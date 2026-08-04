from sqlalchemy.orm import Session
import repositories.product_repository
from fastapi import HTTPException
from schemas.product import ProductCreate, ProductUpdate



def get_product(db:Session, id:int):
    product=repositories.product_repository.product_repository.get(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


def list_products(db:Session):
    return repositories.product_repository.product_repository.get_all(db)

def create_product(db:Session, data: ProductCreate):
    return repositories.product_repository.product_repository.create(db, data.model_dump())


def update_product(db:Session, id:int, data: ProductUpdate):
    product=get_product(db, id)
    return repositories.product_repository.product_repository.update(db, product, data.model_dump(exclude_unset=True))


def delete_product(db:Session, product_id:int):
    product=get_product(db, product_id)
    # check permissions
    # check policies
    return repositories.product_repository.product_repository.delete(db, product)

