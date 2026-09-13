from sqlalchemy.orm import Session
from app.repositories.receipts import get_by_id, get_all, create as repo_create, update as repo_update, delete as repo_delete
from fastapi import HTTPException
from app.schemas.receipts import ReceiptCreate, ReceiptUpdate


def get_receipt(db: Session, id: int):
    receipt = get_by_id(db, id)
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return receipt


def list_receipts(db: Session):
    return get_all(db)


def create_receipt(db: Session, data: ReceiptCreate):
    return repo_create(db, data.model_dump())


def update_receipt(db: Session, id: int, data: ReceiptUpdate):
    receipt = get_receipt(db, id)
    return repo_update(db, receipt, data.model_dump(exclude_unset=True))


def delete_receipt(db: Session, receipt_id: int):
    receipt = get_receipt(db, receipt_id)
    return repo_delete(db, receipt)
