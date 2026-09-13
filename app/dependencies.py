from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.auth_services import get_user_from_token


oauth_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user_from_token(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)):
    user = get_user_from_token(db, token)
    return user
