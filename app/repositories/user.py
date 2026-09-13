from sqlalchemy.orm import Session

from app.models.user import User


def get_all(db: Session):
    return db.query(User).all()


def get_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first() #return none if the user does not exist.


def get_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()#none


def create(db: Session, data: dict):
    user = User(
        username=data.get("username", data.get("name")),
        password=data.get("password"),
        role=data.get("role", "user"),
        phone_number=data.get("phone_number"),
        is_active=data.get("is_active", True),
    )
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