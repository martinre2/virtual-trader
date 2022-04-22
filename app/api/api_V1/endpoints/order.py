from typing import Any

import pendulum
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.helpers.db import get_db
from app.schemas.order import Order, OrderCreate, OrderCreateInDB, Side
from app.schemas.order_position import OrderPositionCreate
from app.schemas.position import PositionCreate, PositionStatus
from app.schemas.user import User
from app.services.market.client import NASDAQClient
from app.utils.jwt import get_current_user

router = APIRouter()


@router.post("/orders", response_model=Order)
def create_order(
    *,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    client: NASDAQClient = Depends(NASDAQClient),
    order_in: OrderCreate
) -> Any:

    quote = client.get_quote(order_in.instrument)
    updated = dict(
        order_in.dict(),
        **{
            "filled_price": quote.primaryData.lastSalePrice,
            "user_id": current_user.id,
        }
    )

    # Check if user have a open position
    position = crud.position.get_open_by_symbol(
        db=db, user_id=current_user.id, instrument=order_in.instrument
    )

    if position and order_in.side == Side.SELL:
        if order_in.qty > position.shares:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Not enough shares to sell.",
            )

    order = crud.order.create(db=db, obj_in=OrderCreateInDB(**updated))

    if not position:
        position_in = PositionCreate(
            instrument=order_in.instrument,
            shares=order_in.qty,
            user_id=current_user.id,
        )

        position = crud.position.create(db=db, obj_in=position_in)
    else:
        # increase shares
        updated_shares = position.shares + (
            order_in.qty * (-1 if order_in.side == Side.SELL else 1)
        )

        position_up = {"shares": updated_shares}

        if updated_shares == 0:
            position_up["status"] = PositionStatus.CLOSED
            position_up["close_at"] = pendulum.now()

        crud.position.update(db, db_obj=position, obj_in=position_up)

    order_position_in = OrderPositionCreate(
        position_id=str(position.id), order_id=str(order.id)
    )

    crud.order_position.create(db=db, obj_in=order_position_in)

    return order
