from sqlalchemy.orm import Session
from app.repositories.suppliers import get_by_id, get_all, create as repo_create, update as repo_update, delete as repo_delete
from fastapi import HTTPException
from app.schemas.suppliers import SupplierCreate, SupplierUpdate


def get_supplier(db: Session, id: int):
    supplier = get_by_id(db, id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier


def list_suppliers(db: Session):
    return get_all(db)


def create_supplier(db: Session, data: SupplierCreate):
    return repo_create(db, data.model_dump())


def update_supplier(db: Session, id: int, data: SupplierUpdate):
    supplier = get_supplier(db, id)
    return repo_update(db, supplier, data.model_dump(exclude_unset=True))


def delete_supplier(db: Session, supplier_id: int):
    supplier = get_supplier(db, supplier_id)
    return repo_delete(db, supplier)
