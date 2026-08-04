from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.sales import Sale

def get_all(db: Session):
    return db.scalars(select(Sale)).all()

def get_by_id(db: Session, item_id: int):
    return db.scalars(select(Sale).where(Sale.id == item_id)).first()

def get_by_name(db: Session, name: str):
    return db.scalars(select(Sale).where(Sale.name == name)).first()

def create(db: Session, name: str, price: float, sku: str, stock: int):
    item = Sale(name=name, price=price, sku=sku, stock=stock)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def update(db: Session, item: Sale, fields: dict):
    for field, value in fields.items():
        setattr(item, field, value)
    db.commit()
    db.refresh(item)
    return item

def delete(db: Session, item: Sale):
    db.delete(item)
    db.commit()
