
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.suppliers import SupplierCreate, SupplierUpdate, SupplierRead
from app.database import get_db
from app.services import suppliers




router = APIRouter(
    prefix="/suppliers",
    tags=["suppliers"])





@router.get("/{supplier_id}", response_model=SupplierRead)
def read_supplier(supplier_id: int, db: Session = Depends(get_db)):
    return suppliers.get_supplier(db, supplier_id)




@router.get("/", response_model=list[SupplierRead])
def list_suppliers(db: Session = Depends(get_db)):
    return suppliers.list_suppliers(db)





@router.post("/", response_model=SupplierRead, status_code=status.HTTP_201_CREATED)
def create_supplier(data:SupplierCreate,db:Session=Depends(get_db)):
    return suppliers.create_supplier(db, data)




@router.put("/{supplier_id}", response_model=SupplierRead)
def update_supplier(supplier_id: int, data: SupplierUpdate, db: Session = Depends(get_db)):
    return suppliers.update_supplier(db, supplier_id, data)




@router.delete("/{supplier_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    return suppliers.delete_supplier(db, supplier_id)
