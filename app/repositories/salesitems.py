from sqlalchemy.orm import Session
from app.models.salesitems import SaleItem

def get_all(db: Session):
    return db.query(SaleItem).all()

def get_by_id(db: Session, item_id: int):
    return db.query(SaleItem).filter(SaleItem.id == item_id).first()

def get_by_name(db: Session, name: str):
    return db.query(SaleItem).filter(SaleItem.name == name).first()

def create(db: Session, name: str, price: float, sku: str, stock: int):
   
    item = SaleItem(name=name, price=price, sku=sku, stock=stock)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def update(db: Session, item: SaleItem, fields: dict):
    for field, value in fields.items():
        setattr(item, field, value)
    db.commit()
    db.refresh(item)
    return item

def delete(db: Session, item: SaleItem):
    db.delete(item)
    db.commit()
