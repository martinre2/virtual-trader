from typing import Any, List

from fastapi import APIRouter

from app.helpers.ticker_price import get_price_by_ticker
from app.schemas.historical_data import HistoricalData

router = APIRouter()


@router.get("/price/{symbol}", response_model=List[HistoricalData])
def get_ticker_price(
    *,
    symbol: str,
) -> Any:
    """
    Get historical price by ticker symbol.
    """

    return get_price_by_ticker(symbol)
