from datetime import datetime
from decimal import Decimal


from schemas.suppliers import SupplierBase
from pydantic import BaseModel, ConfigDict, Field


class SupplierBase(BaseModel):
   name:str
   email:str
   phone:str
   is_active:bool = True


class SupplierCreate(BaseModel):
      pass



class SupplierUpdate(BaseModel):
      name:str | None = None
      email:str | None = None
      phone:str | None = None
      is_active:bool | None = True
      is_active:bool | None = True


class SupplierResponse(SupplierBase):
   model_config=ConfigDict(from_attributes=True)

   id:int
   created_at:datetime
   updated_at:datetime


class SupplierDelete(BaseModel):
      id:int
      model_config=ConfigDict(from_attributes=True)


class SupplierRead(SupplierBase):
        id:int
        created_at:datetime
        updated_at:datetime
        model_config=ConfigDict(from_attributes=True)
          
   
class SupplierCreate(BaseModel):
      pass



class SupplierUpdate(BaseModel):
      name:str | None = None
      email:str | None = None
      phone:str | None = None
      is_active:bool | None = True
      is_active:bool | None = True


class ProductResponse(SupplierBase):
   model_config=ConfigDict(from_attributes=True)

   id:int
   created_at:datetime
   updated_at:datetime
   
   
class UserDelete(BaseModel):
      id:int
      model_config=ConfigDict(from_attributes=True)
      
      
class UserRead(SupplierBase):
        id:int
        created_at:datetime
        updated_at:datetime
        model_config=ConfigDict(from_attributes=True)
          