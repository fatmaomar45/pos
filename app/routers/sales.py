
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.sales import SaleCreate, SaleUpdate, SaleRead, SaleDelete
from app.database import get_db
from app.services import sales




router = APIRouter(
    prefix="/sales",
    tags=["sales"])




@router.get("/", response_model=list[SaleRead])
def list_sales(db: Session = Depends(get_db)):
    return sales.list_sales(db)



@router.post("/", response_model=SaleRead, status_code=status.HTTP_201_CREATED)
def create_sale(data:SaleCreate,db:Session=Depends(get_db)):
    return sales.create_sale(db, data)




@router.put("/{sale_id}", response_model=SaleRead)
def update_sale(sale_id: int, data: SaleUpdate, db: Session = Depends(get_db)):
    return sales.update_sale(db, sale_id, data)




@router.delete("/{sale_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_sale(sale_id: int, db: Session = Depends(get_db)):
    return sales.delete_sale(db, sale_id)
