"""
Historical Data Schema
"""
from pydantic import BaseModel


class HistoricalData(BaseModel):
    """HistoricalData base schema"""

    time: int
    price: str
