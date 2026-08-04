from datetime import datetime
from decimal import Decimal

from schemas.product import BaseModel
from pydantic import BaseModel, ConfigDict, Field
from database import Base

class ProductBase(BaseModel):
   name:str
   sku:str
   price:Decimal
   category:str
   suplier_id:int
   is_active:bool = True


   class productCreate(BaseModel):
      pass



   class productUpdate(BaseModel):
      name:str | None = None
      sku:str | None = None
      price:Decimal | None = None
      category:str | None = None
      suplier_id:int | None = None
      is_active:bool | None = True


class ProductRead(ProductBase):
   model_config=ConfigDict(from_attributes=True)

   id:int
   created_at:datetime
   updated_at:datetime
   
class ProductDelete(ProductBase):
    model_config=ConfigDict(from_attributes=True)
    
    id:int
    created_at:datetime
    updated_at:datetime   