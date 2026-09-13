from sqlalchemy.orm import Session
from app.models.salesitems import SaleItem

def get_all(db: Session):
    return db.query(SaleItem).all()

def get_by_id(db: Session, sale_item_id: int):
    return db.query(SaleItem).filter(SaleItem.sale_item_id == sale_item_id).first()

def get_by_name(db: Session, name: str):
    return db.query(SaleItem).filter(SaleItem.item_type == name).first()

def create(db: Session, data: dict):
    item = SaleItem(
        sale_id=data.get("sale_id"),
        product_id=data.get("product_id"),
        quantity=data.get("quantity"),
        item_type=data.get("item_type", "product"),
        unit_price=data.get("unit_price", 0),
    )
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
