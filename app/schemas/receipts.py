from datetime import datetime
from decimal import Decimal

from schemas.receipts import ReceiptBase
from pydantic import BaseModel, ConfigDict, Field


class ReceiptBase(BaseModel):
   name:str
   sku:str
   price:Decimal
   category:str
   suplier_id:int
   is_active:bool = True


   class ReceiptCreate(BaseModel):
      pass



   class ReceiptUpdate(BaseModel):
      name:str | None = None
      sku:str | None = None
      price:Decimal | None = None
      category:str | None = None
      suplier_id:int | None = None
      is_active:bool | None = True


class ReceiptRead(ReceiptBase):
   model_config=ConfigDict(from_attributes=True)

   id:int
   created_at:datetime
   updated_at:datetime
   
   
class ReceiptDelete(ReceiptBase):
    model_config=ConfigDict(from_attributes=True)
    
    id:int
    created_at:datetime
    updated_at:datetime 
    