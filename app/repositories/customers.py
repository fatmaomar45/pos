from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.customers import Customer  

def get_all(db: Session):
    return db.scalars(select(Customer)).all()

def get_by_id(db: Session, customer_id: int):
    return db.scalars(select(Customer).where(Customer.customer_id == customer_id)).first()

def get_by_email(db: Session, email: str):
    return db.scalars(select(Customer).where(Customer.email == email)).first()

def get_by_phone(db: Session, phone: str):
    return db.scalars(select(Customer).where(Customer.phone == phone)).first()

def create(db: Session, data: dict):
    customer = Customer(
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        email=data.get("email"),
        phone=data.get("phone"),
        address=data.get("address", ""),
        points_balance=data.get("points_balance", 0)
      
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
