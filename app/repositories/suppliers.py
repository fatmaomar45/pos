from sqlalchemy.orm import Session

from app.models.suppliers import Supplier


def get_all(db: Session):
    return db.query(Supplier).all()


def get_by_id(db: Session, supplier_id: int):
    return db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()


def get_by_username(db: Session, username: str):
    return db.query(Supplier).filter(Supplier.supplier_name == username).first()


def create(db: Session, data: dict):
    supplier = Supplier(
        supplier_name=data.get("name"),
        contact_person=data.get("name"),
        phone_number=data.get("phone"),
        email=data.get("email"),
        address=data.get("address", ""),
        password=data.get("password", ""),
        role=data.get("role", "user"),
    )
    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    return supplier


def update(db: Session, supplier: Supplier, fields: dict):
    for field, value in fields.items():
        setattr(supplier, field, value)
    db.commit()
    db.refresh(supplier)
    return supplier


def delete(db: Session, supplier: Supplier):
    db.delete(supplier)
    db.commit()