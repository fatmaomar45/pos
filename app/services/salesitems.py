from sqlalchemy.orm import Session
import repositories.sale_item_repository
from fastapi import HTTPException
from schemas.salesitems import SaleItemCreate, SaleItemUpdate



def get_sale_item(db:Session, id:int):
    sale_item=repositories.sale_item_repository.sale_item_repository.get(db, id)
    if not sale_item:
        raise HTTPException(status_code=404, detail="Sale item not found")
    return sale_item


def list_sale_items(db:Session):
    return repositories.sale_item_repository.sale_item_repository.get_all(db)

def create_sale_item(db:Session, data: SaleItemCreate):
    return repositories.sale_item_repository.sale_item_repository.create(db, data.model_dump())


def update_sale_item(db:Session, id:int, data: SaleItemUpdate):
    sale_item=get_sale_item(db, id)
    return repositories.sale_item_repository.sale_item_repository.update(db, sale_item, data.model_dump(exclude_unset=True))


def delete_sale_item(db:Session, sale_item_id:int):
    sale_item=get_sale_item(db, sale_item_id)
    # check permissions
    # check policies
    return repositories.sale_item_repository.sale_item_repository.delete(db, sale_item)

