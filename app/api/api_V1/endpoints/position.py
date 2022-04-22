from decimal import Decimal
from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.helpers.db import get_db
from app.schemas.order import Side
from app.schemas.user import User
from app.services.market.client import NASDAQClient
from app.utils.decimal import str_to_decimal
from app.utils.jwt import get_current_user

router = APIRouter()


@router.get("/openPositions")
def get_open_positions(
    *,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    client: NASDAQClient = Depends(NASDAQClient),
) -> Any:

    positions = crud.position.get_open_by_user(db=db, user_id=current_user.id)

    positions_summary = []

    for position in positions:

        summary = client.get_summary(position.instrument)
        quote = client.get_quote(position.instrument)

        cum_shares_value = Decimal("0")
        cum_shares = Decimal("0")

        held_shares = str_to_decimal(str(position.shares))

        for order in position.orders:
            if order.side == Side.BUY:
                cum_shares_value += Decimal(order.quantity) * str_to_decimal(
                    order.filled_price
                )
                cum_shares += order.quantity

        avg_price = cum_shares_value / cum_shares
        investment_value = held_shares * avg_price
        current_price = str_to_decimal(quote.primaryData.lastSalePrice)
        current_investment_value = held_shares * current_price

        profit_loss = (current_investment_value / investment_value) - 1

        position_summary = {
            "symbol": position.instrument,
            "profit/loss": "{:.4f}".format(profit_loss),
            "held_shares": position.shares,
            "current_value": "{:.2f}".format(current_investment_value),
            "price_references": {
                "low": summary.summaryData.TodayLow,
                "high": summary.summaryData.TodayHigh,
                "average": summary.summaryData.TodayAvg,
            },
        }

        positions_summary.append(position_summary)

    return positions_summary
