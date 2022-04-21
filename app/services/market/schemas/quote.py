""" NASDAQ Quote Schema """
from pydantic import BaseModel


class PrimaryData(BaseModel):
    """Quote[PrimaryData] Schema"""

    lastSalePrice: str
    netChange: str
    percentageChange: str
    deltaIndicator: str
    lastTradeTimestamp: str
    isRealTime: bool

    def __init__(self, **data):
        data["lastSalePrice"] = data["lastSalePrice"].replace("$", "")
        super().__init__(**data)


class Quote(BaseModel):
    """Quote Schema"""

    symbol: str
    companyName: str
    stockType: str
    exchange: str
    isNasdaqListed: bool
    isNasdaq100: bool
    isHeld: bool
    primaryData: PrimaryData
