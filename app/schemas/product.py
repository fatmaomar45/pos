from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    product_name: str
    sku: str
    cost: int
    category_id: Optional[int] = None
    supplier_id: Optional[int] = None
    is_active: bool = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    product_name: Optional[str] = None
    sku: Optional[str] = None
    cost: Optional[int] = None
    category_id: Optional[int] = None
    supplier_id: Optional[int] = None
    is_active: Optional[bool] = None


class ProductRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    product_id: int
    created_at: datetime


class ProductDelete(BaseModel):
    product_id: int
    model_config = ConfigDict(from_attributes=True)
