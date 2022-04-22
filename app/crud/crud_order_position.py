from app.crud.base import CRUDBase
from app.models.order_position import OrderPosition
from app.schemas.order_position import OrderPositionCreate, OrderPositionUpdate


class CRUDOrderPosition(
    CRUDBase[OrderPosition, OrderPositionCreate, OrderPositionUpdate]
):
    """OrderPosition CRUD class
    Args:
        CRUDBase ([OrderPosition, OrderPositionCreate, OrderPositionUpdate])
    """

    pass


order_position = CRUDOrderPosition(OrderPosition)
