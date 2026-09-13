from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict


class SaleBase(BaseModel):
    customer_id: int
    total_amount: Decimal


class SaleCreate(SaleBase):
    pass


class SaleUpdate(BaseModel):
    customer_id: Optional[int] = None
    total_amount: Optional[Decimal] = None


class SaleRead(SaleBase):
    model_config = ConfigDict(from_attributes=True)

    sale_id: int
    sale_date: datetime


class SaleDelete(BaseModel):
    sale_id: int
    model_config = ConfigDict(from_attributes=True)
