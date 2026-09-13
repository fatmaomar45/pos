from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict


class SaleItemBase(BaseModel):
    sale_id: int
    product_id: int
    quantity: int
    item_type: str
    unit_price: Decimal


class SaleItemCreate(SaleItemBase):
    pass


class SaleItemUpdate(BaseModel):
    sale_id: Optional[int] = None
    product_id: Optional[int] = None
    quantity: Optional[int] = None
    item_type: Optional[str] = None
    unit_price: Optional[Decimal] = None


class SaleItemRead(SaleItemBase):
    model_config = ConfigDict(from_attributes=True)

    sale_item_id: int


class SaleItemDelete(BaseModel):
    sale_item_id: int
    model_config = ConfigDict(from_attributes=True)
