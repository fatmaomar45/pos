from sqlalchemy.orm import Session
from app.repositories.sales import get_by_id, get_all, create as repo_create, update as repo_update, delete as repo_delete
from fastapi import HTTPException
from app.schemas.sales import SaleCreate, SaleUpdate


def get_sale(db: Session, id: int):
    sale = get_by_id(db, id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale


def list_sales(db: Session):
    return get_all(db)


def create_sale(db: Session, data: SaleCreate):
    return repo_create(db, data.model_dump())


def update_sale(db: Session, id: int, data: SaleUpdate):
    sale = get_sale(db, id)
    return repo_update(db, sale, data.model_dump(exclude_unset=True))


def delete_sale(db: Session, sale_id: int):
    sale = get_sale(db, sale_id)
    return repo_delete(db, sale)
