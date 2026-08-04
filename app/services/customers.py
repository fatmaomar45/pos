from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas.customers import CustomerCreate, CustomerUpdate  


def get_customer(db: Session, customer_id: int):  
    customer = customer.get(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

def list_customers(db: Session):
    return list_customers.get_all(db)

def create_customer(db: Session, data: CustomerCreate):
    return customers.create(db, data.model_dump())

def update_customer(db: Session, customer_id: int, data: CustomerUpdate):
    customers = get_customer(db, customer_id)
    return customers.update(db, customers, data.model_dump(exclude_unset=True))

def delete_customer(db: Session, customer_id: int):
    customer = get_customer(db, customer_id)
    return customer.delete(db, customer)
