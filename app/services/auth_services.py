from typing import Any


from fastapi import HTTPException,status
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)

from app.repositories.user import create as create_user, get_by_username, get_by_id
from app.schemas.user import UserCreate


def register(db:Session,data:UserCreate):
    if get_by_username(db,data.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken",
        )
    values=data.model_dump(exclude={"password"})
    values["password"]=hash_password(data.password)
    return create_user(db,values)


def authentication(db:Session,username:str,password:str):
    user=get_by_username(db,username)
    if not user or not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate":"Bearer"},
        )
    return{
        "access_token":create_access_token(user.id),
        "token_type":"bearer",
    }    
    
    
def get_user_from_token(db:Session,token:str):
    credentials_errors=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"},
    )
    try:
        payload:dict[str,Any]=decode_access_token(token)
        subject=payload.get("sub")
        if not isinstance(subject,str) or not subject.strip():
            raise credentials_errors
        user_id=int(subject)
        if user_id <=0:
            raise credentials_errors
    except Exception as e:
        raise credentials_errors from e

    user=get_by_id(db,user_id)
    if user is None:
        raise credentials_errors
    return user