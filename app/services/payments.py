from sqlalchemy.orm import Session
import repositories.payment_repository
from fastapi import HTTPException
from schemas.payments import PaymentCreate, PaymentUpdate



def get_payment(db:Session, id:int):
    payment=repositories.payment_repository.payment_repository.get(db, id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment


def list_payments(db:Session):
    return repositories.payment_repository.payment_repository.get_all(db)

def create_payment(db:Session, data: PaymentCreate):
    return repositories.payment_repository.payment_repository.create(db, data.model_dump())


def update_payment(db:Session, id:int, data: PaymentUpdate):
    payment=get_payment(db, id)
    return repositories.payment_repository.payment_repository.update(db, payment, data.model_dump(exclude_unset=True))


def delete_payment(db:Session, payment_id:int):
    payment=get_payment(db, payment_id)
    # check permissions
    # check policies
    return repositories.payment_repository.payment_repository.delete(db, payment)

