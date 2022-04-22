"""
Order Schema
"""
from typing import Optional

from pydantic import BaseModel


class OrderPositionBase(BaseModel):
    """Position base schema"""

    position_id: Optional[str]
    order_id: Optional[str]


class OrderPositionCreate(OrderPositionBase):
    """Position create schema"""

    position_id: str
    order_id: str


class OrderPositionUpdate(OrderPositionBase):
    pass
