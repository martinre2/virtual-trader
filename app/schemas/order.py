"""
Order Schema
"""
from enum import Enum
from typing import Optional

from pydantic import BaseModel, validator

from app.services.market.client import NASDAQClient


class Side(str, Enum):
    """Side Direction Type"""

    BUY = "BUY"
    SELL = "SELL"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class OrderStatus(str, Enum):
    """Order Status Type"""

    PENDING = "PENDING"
    FILLED = "FILLED"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class OrderType(str, Enum):
    """Order Type"""

    MARKET = "MARKET"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class OrderBase(BaseModel):
    """Order base schema"""

    instrument: Optional[str] = None
    qty: Optional[int] = None
    side: Optional[Side] = None

    @validator("qty")
    def qty_positive(cls, v):
        assert v > 0, "must be PositiveInt"
        return v

    @validator("instrument")
    def instrument_listed(cls, v):
        if v not in NASDAQClient().symbols:
            raise ValueError(f"{v} symbol not exists on the NASDAQ exchange")
        return v


class OrderCreate(OrderBase):
    """Order create schema"""

    instrument: str
    qty: int
    side: Side


class OrderCreateInDB(BaseModel):

    instrument: str
    side: str
    quantity: int
    quantity_buy: int = 0
    quantity_sell: int = 0
    type: OrderType = OrderType.MARKET
    user_id: str
    status: OrderStatus = OrderStatus.PENDING
    filled_price: str

    def __init__(self, **data):
        data["quantity"] = data["qty"]
        if data["side"] == Side.BUY:
            data["quantity_buy"] = data["qty"]
        else:
            data["quantity_sell"] = data["qty"]
        super().__init__(**data)


class OrderUpdate(OrderCreateInDB):
    """Order update schema"""

    pass


class Order(BaseModel):
    instrument: str
    side: str
    quantity: int
    type: OrderType
    status: OrderStatus
    filled_price: str

    class Config:
        orm_mode = True
