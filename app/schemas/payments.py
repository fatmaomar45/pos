from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PaymentBase(BaseModel):
    sale_id: int
    payment_method: str
    amount: Decimal


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    sale_id: Optional[int] = None
    payment_method: Optional[str] = None
    amount: Optional[Decimal] = None


class PaymentRead(PaymentBase):
    model_config = ConfigDict(from_attributes=True)

    payment_id: int
    payment_date: datetime


class PaymentDelete(BaseModel):
    payment_id: int
    model_config = ConfigDict(from_attributes=True)
