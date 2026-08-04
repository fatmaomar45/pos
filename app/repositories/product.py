from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.products import Product  # Assumed model path

def get_all(db: Session):
    return db.scalars(select(Product)).all()

def get_by_id(db: Session, product_id: int):
    return db.scalars(select(Product).where(Product.id == product_id)).first()

def get_by_sku(db: Session, sku: str):
    return db.scalars(select(Product).where(Product.sku == sku)).first()

def create(db: Session, name: str, sku: str, price: float, category: str = None, description: str = None):
    product = Product(
        name=name,
        sku=sku,
        price=price,
        category=category,
        description=description
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def update(db: Session, product: Product, fields: dict):
    for field, value in fields.items():
        setattr(product, field, value)
    db.commit()
    db.refresh(product)
    return product

def delete(db: Session, product: Product):
    db.delete(product)
    db.commit()
