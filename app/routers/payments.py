
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.payments import PaymentCreate, PaymentUpdate, PaymentRead, PaymentDelete
from app.database import get_db
from app.services import payments




router = APIRouter(
    prefix="/payments",
    tags=["payments"])


@router.get("/{payment_id}", response_model=PaymentRead)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    return payments.get_payment(db, payment_id)


@router.get("/", response_model=list[PaymentRead])
def list_payments(db: Session = Depends(get_db)):
    return payments.list_payments(db)


@router.post("/", response_model=PaymentRead, status_code=status.HTTP_201_CREATED)
def create_payment(data:PaymentCreate,db:Session=Depends(get_db)):
    return payments.create_payment(db, data)



@router.put("/{payment_id}", response_model=PaymentRead)
def update_payment(payment_id: int, data: PaymentUpdate, db: Session = Depends(get_db)):
    return payments.update_payment(db, payment_id, data)



@router.delete("/{payment_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    return payments.delete_payment(db, payment_id)
