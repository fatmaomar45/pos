from datetime import datetime
from decimal import Decimal

from schemas.salesitems import SaleItemBase
from pydantic import BaseModel, ConfigDict, Field


class SaleItemBase(BaseModel):
   name:str
   sku:str
   price:Decimal
   category:str
   suplier_id:int
   is_active:bool = True


   class SaleItemCreate(BaseModel):
      pass



   class SaleItemUpdate(BaseModel):
      name:str | None = None
      sku:str | None = None
      price:Decimal | None = None
      category:str | None = None
      suplier_id:int | None = None
      is_active:bool | None = True


class SaleItemResponse(SaleItemBase):
   model_config=ConfigDict(from_attributes=True)

   id:int
   created_at:datetime
   updated_at:datetime
   
class SaleItemDelete(SaleItemBase):
    model_config=ConfigDict(from_attributes=True)
    
    id:int
    created_at:datetime
    updated_at:datetime   