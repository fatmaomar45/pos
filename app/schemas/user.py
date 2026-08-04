from datetime import datetime
from decimal import Decimal

from schemas.product import UserBase
from database import Base
from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
   name:str
   email:str
   password:str
   is_active:bool = True


class UserCreate(BaseModel):
      pass



class UserUpdate(BaseModel):
      name:str | None = None
      email:str | None = None
      password:str | None = None
      is_active:bool | None = True
      is_active:bool | None = True


class UserResponse(UserBase):
   model_config=ConfigDict(from_attributes=True)

   id:int
   created_at:datetime
   updated_at:datetime
   
   
class UserDelete(BaseModel):
      id:int
      model_config=ConfigDict(from_attributes=True)
      
      
class UserRead(UserBase):
        id:int
        created_at:datetime
        updated_at:datetime
        model_config=ConfigDict(from_attributes=True)
          