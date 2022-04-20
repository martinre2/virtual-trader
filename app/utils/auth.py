from typing import Optional

from passlib.context import CryptContext

from app.db.users import fake_users_db
from app.schemas.user import UserInDB

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def authenticate_user(username: str, password: str):
    """Authenticate

    Args:
        username (str):
        password (str):

    Returns:
        Union[bool, User]: returns a user if credential matchs
    """
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def get_user(username: Optional[str]):
    """Retrive user from storage"""
    if username in fake_users_db:
        user_dict = fake_users_db[username]
        return UserInDB(**user_dict)


def verify_password(plain_password, hashed_password):
    """Simple pasword verifier"""
    return pwd_context.verify(plain_password, hashed_password)
