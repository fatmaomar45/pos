from sqlalchemy.orm import Session

from app.models.suppliers import Supplier


def get_all(db: Session):
    return db.query(Supplier).all()


def get_by_id(db: Session, user_id: int):
    return db.query(Supplier).filter(Supplier.id == user_id).first()


def get_by_username(db: Session, username: str):
    return db.query(Supplier).filter(Supplier.username == username).first()


def create(db: Session, username: str, hashed_password: str, role: str, email: str):
    supplier = Supplier(username=username, hashed_password=hashed_password, role=role, email=email)
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


def delete(db: Session, user: Supplier):
    db.delete(Supplier)
    db.commit()