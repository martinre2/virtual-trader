"""Position model"""
from uuid import uuid4

from sqlalchemy import Column, DateTime, Enum, Integer, Text, text

from app.db.base_class import Base


class Position(Base):

    id = Column(Text(length=36), default=lambda: str(uuid4()), primary_key=True)
    user_id = Column(Text(length=36), nullable=False)
    instrument = Column(Text(12), nullable=False)
    shares = Column(Integer, nullable=False)
    status = Column(
        Enum("OPEN", "CLOSED"),
        server_default=text("OPEN"),
    )
    open_at = Column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    close_at = Column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
