"""
Main file for FastAPI App
"""
import secure
import sentry_sdk
from fastapi import FastAPI, HTTPException, Request, Response
from psycopg2 import OperationalError
from retrying import retry

from app import __version__
from app.api import healthcheck
from app.api.api_V1.api import api_router
from app.config.logger import init_logging
from app.config.settings import settings
from app.db.session import SessionLocal
from app.utils.exceptions import DeployError

if settings.environment in (
    "production",
    "staging",
):
    sentry_sdk.init(
        settings.sentry_url,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
        environment=settings.environment,
    )

secure_headers = secure.Secure()

fastapi_app = FastAPI(
    title="virtual-trader",
    description="NASDAQ virtual trading environment",
    version=__version__,
)

fastapi_app.add_event_handler("startup", init_logging)


@fastapi_app.middleware("http")
@retry(
    retry_on_result=DeployError.db_starting_up,
    wait_fixed=10000,
    stop_max_attempt_number=3,
)
async def db_session_middleware(request: Request, call_next):
    """Stablish DB sessions per request"""
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    except OperationalError as e:
        DeployError.db_starting_up(e)
    finally:
        request.state.db.close()
    return response


@fastapi_app.middleware("http")
async def set_secure_headers(request, call_next):
    """
    Secure headers middleware
    """
    response = await call_next(request)
    secure_headers.framework.fastapi(response)
    return response


@fastapi_app.exception_handler(HTTPException)
async def sentry_http_exception_handler(request, e):
    """
    Catch exceptions from HTTP
    """
    with sentry_sdk.configure_scope() as scope:
        scope.set_context("request", request)
        sentry_sdk.capture_exception(e)

    return Response(str(e.detail), status_code=e.status_code)


fastapi_app.include_router(healthcheck.router)
fastapi_app.include_router(api_router, prefix="/api/v1")

app = fastapi_app
