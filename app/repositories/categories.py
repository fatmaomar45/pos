from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.categories import Category 

def get_all(db: Session):
    return db.scalars(select(Category)).all()

def get_by_id(db: Session, category_id: int):
    return db.scalars(select(Category).where(Category.id == category_id)).first()

def get_by_slug(db: Session, slug: str):

    return db.scalars(select(Category).where(Category.slug == slug)).first()

def create(db: Session, name: str, slug: str, description: str = None, parent_id: int = None):
    category = Category(
        name=name,
        slug=slug,
        description=description,
        parent_id=parent_id  
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
