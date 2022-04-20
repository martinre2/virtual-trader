from fastapi import APIRouter, Depends

from app.schemas.user import User
from app.utils.jwt import get_current_user

router = APIRouter()


@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    """Get the belongs user requester

    Args:
        current_user (User, optional): get sub from jwt token

    Returns:
        current_user
    """
    return current_user
