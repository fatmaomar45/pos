from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    password: str
    role: str
    phone_number: Optional[str] = None
    is_active: bool = True


class UserCreate(UserBase):
    password:str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None
    phone_number: Optional[str] = None
    is_active: Optional[bool] = None


class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    created_at: datetime
    updated_at: datetime
    is_active:bool


class UserDelete(BaseModel):
    user_id: int
    model_config = ConfigDict(from_attributes=True)
