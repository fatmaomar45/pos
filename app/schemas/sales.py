from datetime import datetime
from decimal import Decimal


from database import Base
from schemas.sales import SaleBase
from pydantic import BaseModel, ConfigDict, Field


class SaleBase(BaseModel):
   name:str
   sku:str
   price:Decimal
   category:str
   suplier_id:int
   is_active:bool = True


   class SaleCreate(BaseModel):
      pass



   class SaleUpdate(BaseModel):
      name:str | None = None
      sku:str | None = None
      price:Decimal | None = None
      category:str | None = None
      suplier_id:int | None = None
      is_active:bool | None = True


class SaleResponse(SaleBase):
   model_config=ConfigDict(from_attributes=True)

   id:int
   created_at:datetime
   updated_at:datetime
   
class SaleDelete(SaleBase):
    model_config=ConfigDict(from_attributes=True)
    
    id:int
    created_at:datetime
    updated_at:datetime
       