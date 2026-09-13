from sqlalchemy.orm import Session
from app.repositories.customers import get_by_id, get_all, create as repo_create, update as repo_update, delete as repo_delete
from fastapi import HTTPException
from app.schemas.customers import CustomerCreate, CustomerUpdate


def get_customer(db: Session, customer_id: int):
    customer = get_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


def list_customers(db: Session):
    return get_all(db)


def create_customer(db: Session, data: CustomerCreate):
    return repo_create(db, data.model_dump())


def update_customer(db: Session, customer_id: int, data: CustomerUpdate):
    customer = get_customer(db, customer_id)
    return repo_update(db, customer, data.model_dump(exclude_unset=True))


def delete_customer(db: Session, customer_id: int):
    customer = get_customer(db, customer_id)
    return repo_delete(db, customer)
