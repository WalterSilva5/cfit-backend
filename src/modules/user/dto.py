from typing import Any
from pydantic import BaseModel, EmailStr
from typing import Any, Union
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    hashed_password: str

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool
    created_at: Union[str, Any]
    updated_at: Union[str, None]
    role: str

class UserLogin(BaseModel):
    email: str
    hashed_password: str
    role: str

class UpdatePasswordRequest(BaseModel):
    email: EmailStr
    hashed_password: str
