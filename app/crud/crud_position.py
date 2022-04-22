from typing import List, Optional

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.position import Position
from app.schemas.position import PositionCreate, PositionStatus, PositionUpdate


class CRUDPosition(CRUDBase[Position, PositionCreate, PositionUpdate]):
    """Order CRUD class
    Args:
        CRUDBase ([Order, OrderCreateInDB])
    """

    def get_open_by_symbol(
        self,
        db: Session,
        user_id: str,
        instrument: str,
    ) -> Optional[Position]:
        """Get open position by user and symbol

        Args:
            db (Session):
            user_id (str):
            instrument (str):

        Returns:
            Optional[Position]:
        """

        return (
            db.query(self.model)
            .filter(
                and_(
                    self.model.user_id == user_id,
                    self.model.instrument == instrument,
                    self.model.status == PositionStatus.OPEN,
                )
            )
            .first()
        )

    def get_open_by_user(
        self,
        db: Session,
        user_id: str,
    ) -> List[Position]:
        """Get open position by user

        Args:
            db (Session):
            user_id (str):

        Returns:
            List[Position]:
        """

        return (
            db.query(self.model)
            .filter(
                and_(
                    self.model.user_id == user_id,
                    self.model.status == PositionStatus.OPEN,
                )
            )
            .all()
        )


position = CRUDPosition(Position)
