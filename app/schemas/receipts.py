from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ReceiptBase(BaseModel):
    sale_id: int
    receipt_number: str


class ReceiptCreate(ReceiptBase):
    pass


class ReceiptUpdate(BaseModel):
    sale_id: Optional[int] = None
    receipt_number: Optional[str] = None


class ReceiptRead(ReceiptBase):
    model_config = ConfigDict(from_attributes=True)

    receipt_id: int
    issue_date: datetime


class ReceiptDelete(BaseModel):
    receipt_id: int
    model_config = ConfigDict(from_attributes=True)
