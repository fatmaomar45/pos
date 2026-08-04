from sqlalchemy.orm import Session
import repositories.supplier_repository
from fastapi import HTTPException
from schemas.product import SupplierCreate, SupplierUpdate



def get_supplier(db:Session, id:int):
    supplier=repositories.supplier_repository.supplier_repository.get(db, id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier


def list_suppliers(db:Session):
    return repositories.supplier_repository.supplier_repository.get_all(db)

def create_supplier(db:Session, data: SupplierCreate):
    return repositories.supplier_repository.supplier_repository.create(db, data.model_dump())


def update_supplier(db:Session, id:int, data: SupplierUpdate):
    supplier=get_supplier(db, id)
    return repositories.supplier_repository.supplier_repository.update(db, supplier, data.model_dump(exclude_unset=True))


def delete_supplier(db:Session, supplier_id:int):
    supplier=get_supplier(db, supplier_id)
    # check permissions
    # check policies
    return repositories.supplier_repository.supplier_repository.delete(db, supplier)

