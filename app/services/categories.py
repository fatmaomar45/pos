from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas.categories import CategoryCreate, CategoryUpdate  


def get_category(db: Session, category_id: int):  
    category = category.get(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

def list_categories(db: Session):
    return list_categories.get_all(db)

def create_category(db: Session, data: CategoryCreate):
    return categories.create(db, data.model_dump())

def update_category(db: Session, category_id: int, data: CategoryUpdate):
    category = get_category(db, category_id)
    return category.update(db, category, data.model_dump(exclude_unset=True))

def delete_category(db: Session, category_id: int):
    category = get_category(db, category_id)
    return category.delete(db, category)
