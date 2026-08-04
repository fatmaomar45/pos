from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.customers import Customer  

def get_all(db: Session):
    return db.scalars(select(Customer)).all()

def get_by_id(db: Session, customer_id: int):
    return db.scalars(select(Customer).where(Customer.id == customer_id)).first()

def get_by_email(db: Session, email: str):
    return db.scalars(select(Customer).where(Customer.email == email)).first()

def get_by_phone(db: Session, phone: str):
    return db.scalars(select(Customer).where(Customer.phone == phone)).first()

def create(db: Session, first_name: str, last_name: str, email: str = None, phone: str = None, loyalty_tier: str = "bronze"):
    customer = Customer(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        loyalty_tier=loyalty_tier,
        created_at=datetime.utcnow()
    )
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def update(db: Session, customer: Customer, fields: dict):
    for field, value in fields.items():
        setattr(customer, field, value)
    db.commit()
    db.refresh(customer)
    return customer

def delete(db: Session, customer: Customer):
    db.delete(customer)
    db.commit()
