from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class SupplierBase(BaseModel):
    supplier_name: str
    contact_person: str
    phone_number: str
    email: str
    address: str
    password: str
    role: str


class SupplierCreate(SupplierBase):
    pass


class SupplierUpdate(BaseModel):
    supplier_name: Optional[str] = None
    contact_person: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None


class SupplierRead(SupplierBase):
    model_config = ConfigDict(from_attributes=True)

    supplier_id: int


class SupplierDelete(BaseModel):
    supplier_id: int
    model_config = ConfigDict(from_attributes=True)
