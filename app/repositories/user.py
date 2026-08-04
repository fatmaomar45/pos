from sqlalchemy.orm import Session

from app.models.user import User


def get_all(db: Session):
    return db.query(User).all()


def get_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create(db: Session, username: str, hashed_password: str, role: str, email: str):
    user = User(username=username, hashed_password=hashed_password, role=role, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update(db: Session, user: User, fields: dict):
    for field, value in fields.items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user


def delete(db: Session, user: User):
    db.delete(user)
    db.commit()