from sqlalchemy.orm import Session
import repositories.receipt_repository
from fastapi import HTTPException
from schemas.receipts import ReceiptCreate, ReceiptUpdate



def get_receipt(db:Session, id:int):
    receipt=repositories.receipt_repository.receipt_repository.get(db, id)
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return receipt


def list_receipts(db:Session):
    return repositories.receipt_repository.receipt_repository.get_all(db)

def create_receipt(db:Session, data: ReceiptCreate):
    return repositories.receipt_repository.receipt_repository.create(db, data.model_dump())


def update_receipt(db:Session, id:int, data: ReceiptUpdate):
    receipt=get_receipt(db, id)
    return repositories.receipt_repository.receipt_repository.update(db, receipt, data.model_dump(exclude_unset=True))


def delete_receipt(db:Session, receipt_id:int):
    receipt=get_receipt(db, receipt_id)
    # check permissions
    # check policies
    return repositories.receipt_repository.receipt_repository.delete(db, receipt)

