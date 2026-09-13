from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.sales import Sale

def get_all(db: Session):
    return db.scalars(select(Sale)).all()

def get_by_id(db: Session, sale_id: int):
    return db.scalars(select(Sale).where(Sale.sale_id == sale_id)).first()

def get_by_name(db: Session, name: str):
    return db.scalars(select(Sale).where(Sale.customer_id == name)).first()

def create(db: Session, data: dict):
    sale = Sale(
        customer_id=data.get("customer_id"),
        total_amount=data.get("total_amount", 0),
    )
    db.add(sale)
    db.commit()
    db.refresh(sale)
    return sale

def update(db: Session, sale: Sale, fields: dict):
    for field, value in fields.items():
        setattr(sale, field, value)
    db.commit()
    db.refresh(sale)
    return sale

def delete(db: Session, sale: Sale):
    db.delete(sale)
    db.commit()
