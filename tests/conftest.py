from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base_class import Base
from app.helpers.db import get_db
from app.main import fastapi_app
from app.schemas.user import UserInDB
from app.utils.jwt import get_current_user

DATABASE_URL = "sqlite:///./test.db"

"""
Setup sqlite db for tests
"""

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

Base.metadata.create_all(bind=engine)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def override_get_current_user():
    """Get test user"""
    return UserInDB(
        id="00000000-0000-0000-0000-000000000001",
        username="tester",
        hashed_password="###",
    )


@pytest.fixture(scope="session")
def db() -> Generator:
    yield TestingSessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    """Override test client with local db

    Yields:
        Generator: TestClient
    """
    fastapi_app.dependency_overrides[get_db] = override_get_db
    fastapi_app.dependency_overrides[
        get_current_user
    ] = override_get_current_user

    with TestClient(fastapi_app) as c:
        yield c
