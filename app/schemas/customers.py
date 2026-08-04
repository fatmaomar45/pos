from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str


class CustomerCreate(CustomerBase):
    points_balance: int = 0


class CustomerUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    points_balance: Optional[int] = None


class CustomerRead(CustomerBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    points_balance: int