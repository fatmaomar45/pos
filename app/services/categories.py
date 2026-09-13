from sqlalchemy.orm import Session
from app.repositories.categories import get_by_id, get_all, create as repo_create, update as repo_update, delete as repo_delete
from fastapi import HTTPException
from app.schemas.categories import CategoryCreate, CategoryUpdate


def get_category(db: Session, category_id: int):
    category = get_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


def list_categories(db: Session):
    return get_all(db)


def create_category(db: Session, data: CategoryCreate):
    return repo_create(db, data.model_dump())


def update_category(db: Session, category_id: int, data: CategoryUpdate):
    category = get_category(db, category_id)
    return repo_update(db, category, data.model_dump(exclude_unset=True))


def delete_category(db: Session, category_id: int):
    category = get_category(db, category_id)
    return repo_delete(db, category)
