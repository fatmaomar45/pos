from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.receipts import Receipt  

def get_all(db: Session):
    return db.scalars(select(Receipt)).all()

def get_by_id(db: Session, receipt_id: int):
    return db.scalars(select(Receipt).where(Receipt.id == receipt_id)).first()

def get_by_receipt_number(db: Session, receipt_number: str):
    return db.scalars(select(Receipt).where(Receipt.receipt_number == receipt_number)).first()

def create(db: Session, receipt_number: str, total_amount: float, tax_amount: float, payment_method: str):
    receipt = Receipt(
        receipt_number=receipt_number,
        total_amount=total_amount,
        tax_amount=tax_amount,
        payment_method=payment_method,
        created_at=datetime.utcnow()
    )
    db.add(receipt)
    db.commit()
    db.refresh(receipt)
    return receipt

def update(db: Session, receipt: Receipt, fields: dict):
    for field, value in fields.items():
        setattr(receipt, field, value)
    db.commit()
    db.refresh(receipt)
    return receipt

def delete(db: Session, receipt: Receipt):
    db.delete(receipt)
    db.commit()
