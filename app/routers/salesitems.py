
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.salesitems import SaleItemCreate, SaleItemUpdate, SaleItemRead
from app.database import get_db
from app.services import salesitems



router = APIRouter(
    prefix="/salesitems",
    tags=["salesitems"])


@router.get("/{sale_item_id}", response_model=SaleItemRead)
def read_sale_item(sale_item_id: int, db: Session = Depends(get_db)):
    return salesitems.get_sale_item(db, sale_item_id)


@router.get("/", response_model=list[SaleItemRead])
def list_sale_items(db: Session = Depends(get_db)):
    return salesitems.list_sale_items(db)


@router.post("/", response_model=SaleItemRead, status_code=status.HTTP_201_CREATED)
def create_sale_item(data:SaleItemCreate,db:Session=Depends(get_db)):
    return salesitems.create_sale_item(db, data)


@router.put("/{sale_item_id}", response_model=SaleItemRead)
def update_sale_item(sale_item_id: int, data: SaleItemUpdate, db: Session = Depends(get_db)):
    return salesitems.update_sale_item(db, sale_item_id, data)


@router.delete("/{sale_item_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_sale_item(sale_item_id: int, db: Session = Depends(get_db)):
    return salesitems.delete_sale_item(db, sale_item_id)
