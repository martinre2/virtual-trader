"""
User Schema
"""
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    """User base schema"""

    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    id: str
    hashed_password: str
