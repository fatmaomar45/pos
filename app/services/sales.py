from sqlalchemy.orm import Session
import repositories.sale_repository
from fastapi import HTTPException
from schemas.sales import SaleCreate, SaleUpdate



def get_sale(db:Session, id:int):
    sale=repositories.sale_repository.sale_repository.get(db, id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale


def list_sales(db:Session):
    return repositories.sale_repository.sale_repository.get_all(db)

def create_sale(db:Session, data: SaleCreate):
    return repositories.sale_repository.sale_repository.create(db, data.model_dump())


def update_sale(db:Session, id:int, data: SaleUpdate):
    sale=get_sale(db, id)
    return repositories.sale_repository.sale_repository.update(db, sale, data.model_dump(exclude_unset=True))


def delete_sale(db:Session, sale_id:int):
    sale=get_sale(db, sale_id)
    # check permissions
    # check policies
    return repositories.sale_repository.sale_repository.delete(db, sale)

