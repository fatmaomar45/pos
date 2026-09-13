from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.payments import Payment 

def get_all(db: Session):
    return db.scalars(select(Payment)).all()

def get_by_id(db: Session, payment_id: int):
    return db.scalars(select(Payment).where(Payment.payment_id == payment_id)).first()

def get_by_receipt_id(db: Session, receipt_id: int):
    
    return db.scalars(select(Payment).where(Payment.sale_id == receipt_id)).all()

def create(db: Session, data: dict):
    payment = Payment(
        sale_id=data.get("sale_id"),
        payment_method=data.get("payment_method"),
        amount=data.get("amount", data.get("amount_paid", 0)),
        payment_date=datetime.utcnow()
    )
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment

def update(db: Session, payment: Payment, fields: dict):
    for field, value in fields.items():
        setattr(payment, field, value)
    db.commit()
    db.refresh(payment)
    return payment

def delete(db: Session, payment: Payment):
    db.delete(payment)
    db.commit()
