from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.user import get_by_id, get_all, get_by_username, create as repo_create, update as repo_update, delete as repo_delete
from app.schemas.user import UserCreate, UserUpdate


def get_user(db: Session, id: int):
    user = get_by_id(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def list_users(db: Session):
    return get_all(db)


def create_user(db: Session, data: UserCreate):
    if get_by_username(db, data.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    return repo_create(db, data.model_dump())


def update_user(db: Session, id: int, data: UserUpdate):
    user = get_user(db, id)
    fields_to_update = data.model_dump(exclude_unset=True)
    if "username" in fields_to_update:
        existing_user = get_by_username(db, fields_to_update["username"])
        if existing_user and existing_user.user_id != id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    return repo_update(db, user, data.model_dump(exclude_unset=True))


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    return repo_delete(db, user)
