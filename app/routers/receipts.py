
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.receipts import ReceiptCreate, ReceiptRead
from app.database import get_db
from app.services import receipts



router = APIRouter(
    prefix="/receipts",
    tags=["receipts"])


@router.get("/{receipt_id}", response_model=ReceiptRead)
def read_receipt(receipt_id: int, db: Session = Depends(get_db)):
    return receipts.get_receipt(db, receipt_id)


@router.get("/", response_model=list[ReceiptRead])
def list_receipts(db: Session = Depends(get_db)):
    return receipts.list_receipts(db)


@router.post("/", response_model=ReceiptRead, status_code=status.HTTP_201_CREATED)
def create_receipt(data:ReceiptCreate,db:Session=Depends(get_db)):
    return receipts.create_receipt(db, data)
