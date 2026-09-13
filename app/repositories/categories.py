from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.categories import Category 

def get_all(db: Session):
    return db.scalars(select(Category)).all()

def get_by_id(db: Session, category_id: int):
    return db.scalars(select(Category).where(Category.category_id == category_id)).first()

def get_by_slug(db: Session, slug: str):

    return db.scalars(select(Category).where(Category.category_name == slug)).first()

def create(db: Session, data: dict):
    category = Category(
        name=data.get("name"),
        description=data.get("description"),
    )
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def update(db: Session, category: Category, fields: dict):
    for field, value in fields.items():
        setattr(category, field, value)
    db.commit()
    db.refresh(category)
    return category

def delete(db: Session, category: Category):
    db.delete(category)
    db.commit()
