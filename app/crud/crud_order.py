from app.crud.base import CRUDBase
from app.models.order import Order
from app.schemas.order import OrderCreateInDB, OrderUpdate


class CRUDOrder(CRUDBase[Order, OrderCreateInDB, OrderUpdate]):
    """Order CRUD class
    Args:
        CRUDBase ([Order, OrderCreateInDB])
    """

    pass


order = CRUDOrder(Order)
