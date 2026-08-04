
from fastapi import FastAPI
from app.database import Session
from sqlalchemy.orm import Session
from app.models.product import Product


class ProductRepository:
    def __init__(self):
        self.model=Product


def get(self,db:Session, id:int):
    return db.get(  Product,_id)


def get_all(self,db:Session):
    return db.query(Product).all()


def create( self,db:Session, product:ProductCreate):
    product=Product(**data)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update(self,db:Session, db_obj:Product, data:dict):
    for field,value in data.dict().items():
        setattr(db_obj,field,value)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete(self,db:Session, db_obj:Product):
    db.delete(db_obj)
    db.commit()

    product_repository=ProductRepository()