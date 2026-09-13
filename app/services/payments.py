from sqlalchemy.orm import Session
from app.repositories.payments import get_by_id, get_all, create as repo_create, update as repo_update, delete as repo_delete
from fastapi import HTTPException
from app.schemas.payments import PaymentCreate, PaymentUpdate


def get_payment(db: Session, id: int):
    payment = get_by_id(db, id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment


def list_payments(db: Session):
    return get_all(db)


def create_payment(db: Session, data: PaymentCreate):
    return repo_create(db, data.model_dump())


def update_payment(db: Session, id: int, data: PaymentUpdate):
    payment = get_payment(db, id)
    return repo_update(db, payment, data.model_dump(exclude_unset=True))


def delete_payment(db: Session, payment_id: int):
    payment = get_payment(db, payment_id)
    return repo_delete(db, payment)
