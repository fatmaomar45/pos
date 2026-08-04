from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.payments import Payment 

def get_all(db: Session):
    return db.scalars(select(Payment)).all()

def get_by_id(db: Session, payment_id: int):
    return db.scalars(select(Payment).where(Payment.id == payment_id)).first()

def get_by_receipt_id(db: Session, receipt_id: int):
    
    return db.scalars(select(Payment).where(Payment.receipt_id == receipt_id)).all()

def create(db: Session, receipt_id: int, amount: float, payment_method: str, status: str = "completed", transaction_reference: str = None):
    payment = Payment(
        receipt_id=receipt_id,
        amount=amount,
        payment_method=payment_method,  
        status=status,                 
        transaction_reference=transaction_reference
        
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
