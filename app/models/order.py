""" Order Model"""
from uuid import uuid4

from sqlalchemy import Column, Enum, Integer, Text, text

from app.db.base_class import Base


class Order(Base):

    id = Column(Text(length=36), default=lambda: str(uuid4()), primary_key=True)
    instrument = Column(Text(12), nullable=False)
    side = Column(
        Enum("BUY", "SELL"),
        server_default=text("BUY"),
    )
    quantity = Column(Integer, nullable=False)
    quantity_buy = Column(Integer, nullable=False, server_default=text("0"))
    quantity_sell = Column(Integer, nullable=False, server_default=text("0"))
    type = Column(Text(12), nullable=False)
    user_id = Column(Text(length=36), nullable=False)
    status = Column(
        Enum("PENDING", "FILLED"),
        server_default=text("PENDING"),
    )
    filled_price = Column(Text(12), server_default=text("0.00"))
