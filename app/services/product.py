from sqlalchemy.orm import Session
from app.repositories.products import get_by_id, get_all, create as repo_create, update as repo_update, delete as repo_delete
from fastapi import HTTPException
from app.schemas.product import ProductCreate, ProductUpdate


def get_product(db: Session, id: int):
    product = get_by_id(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


def list_products(db: Session):
    return get_all(db)


def create_product(db: Session, data: ProductCreate):
    return repo_create(db, data.model_dump())


def update_product(db: Session, id: int, data: ProductUpdate):
    product = get_product(db, id)
    return repo_update(db, product, data.model_dump(exclude_unset=True))


def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    return repo_delete(db, product)
