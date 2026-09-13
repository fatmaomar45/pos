from sqlalchemy.orm import Session
from app.repositories.salesitems import get_by_id, get_all, create as repo_create, update as repo_update, delete as repo_delete
from fastapi import HTTPException
from app.schemas.salesitems import SaleItemCreate, SaleItemUpdate


def get_sale_item(db: Session, id: int):
    sale_item = get_by_id(db, id)
    if not sale_item:
        raise HTTPException(status_code=404, detail="Sale item not found")
    return sale_item


def list_sale_items(db: Session):
    return get_all(db)


def create_sale_item(db: Session, data: SaleItemCreate):
    return repo_create(db, data.model_dump())


def update_sale_item(db: Session, id: int, data: SaleItemUpdate):
    sale_item = get_sale_item(db, id)
    return repo_update(db, sale_item, data.model_dump(exclude_unset=True))


def delete_sale_item(db: Session, sale_item_id: int):
    sale_item = get_sale_item(db, sale_item_id)
    return repo_delete(db, sale_item)
