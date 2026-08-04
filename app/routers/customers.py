
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.customers import CustomerCreate, CustomerUpdate, CustomerRead
from app.database import get_db
from app.services import customers




router = APIRouter(
    prefix="/customers",
    tags=["customers"])



@router.get("/{customer_id}", response_model=CustomerRead)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    return customers.get_customer(db, customer_id)


@router.get("/", response_model=list[CustomerRead])
def list_customers(db: Session = Depends(get_db)):
    return customers.list_customers(db)



@router.post("/", response_model=CustomerRead, status_code=status.HTTP_201_CREATED)
def create_customer(data:CustomerCreate,db:Session=Depends(get_db)):
    return customers.create_customer(db, data)




@router.put("/{customer_id}", response_model=CustomerRead)
def update_customer(customer_id: int, data: CustomerUpdate, db: Session = Depends(get_db)):
    return customers.update_customer(db, customer_id, data)




@router.delete("/{customer_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    return customers.delete_customer(db, customer_id)
