"""
Order Schema
"""
from enum import Enum
from typing import Optional

import pendulum
from pydantic import BaseModel
from pydantic.schema import datetime


class PositionStatus(str, Enum):
    """Position Status Type"""

    OPEN = "OPEN"
    CLOSED = "CLOSED"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class PositionBase(BaseModel):
    """Position base schema"""

    user_id: Optional[str]
    instrument: Optional[str]
    shares: Optional[int]
    status: Optional[PositionStatus]
    open_at: Optional[datetime]
    close_at: Optional[datetime]


class PositionCreate(PositionBase):
    """Position create schema"""

    user_id: str
    instrument: str
    shares: int
    status: PositionStatus = PositionStatus.OPEN
    open_at: datetime = pendulum.now()


class PositionUpdate(PositionBase):
    pass
