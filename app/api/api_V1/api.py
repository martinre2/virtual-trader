"""
Application API routes
"""
from fastapi import APIRouter, status

from app.api.api_V1.endpoints import auth, items, order, user

api_router = APIRouter()

api_router.include_router(
    items.router,
    prefix="/items",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


api_router.include_router(
    auth.router,
    prefix="/auth",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
    tags=["auth"],
)

api_router.include_router(
    user.router,
    prefix="/user",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
    tags=["auth"],
)


api_router.include_router(
    order.router,
    prefix="/exchange",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
    tags=["exchange"],
)
