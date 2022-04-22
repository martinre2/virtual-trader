from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class OrderPosition(Base):
    __tablename__ = "order_position"

    id = Column(Text(length=36), default=lambda: str(uuid4()), primary_key=True)
    position_id = Column(ForeignKey("position.id"), nullable=False)
    order_id = Column(ForeignKey("order.id"), nullable=False)

    order = relationship("Order")
    position = relationship("Position")
