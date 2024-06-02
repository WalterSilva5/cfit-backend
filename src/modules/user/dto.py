from typing import Any
from pydantic import BaseModel, EmailStr
from typing import Any, Union
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool
    created_at: Union[str, Any]
    updated_at: Union[str, None]
  

    class Config:
        orm_mode = True
