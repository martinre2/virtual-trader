from app.crud.base import CRUDBase
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    """Item CRUD class
    Args:
        CRUDBase ([Item, ItemCreate, ItemUpdate])
    """

    pass


item = CRUDItem(Item)
