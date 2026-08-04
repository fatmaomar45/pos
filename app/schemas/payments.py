from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PaymentBase(BaseModel):
    sale_id: int
    payment_method: str
    amount_paid: Decimal


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    payment_method: Optional[str] = None
    amount_paid: Optional[Decimal] = None


class PaymentRead(PaymentBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    payment_date: datetime