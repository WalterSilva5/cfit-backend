from fastapi import HTTPException
from passlib.context import CryptContext
from pydantic import EmailStr
from src.modules.user.dto import UserCreate
from src.modules.user import repository
from src.models.users_model import User as UserModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_all(page: int = 1, per_page: int = 10):
    return repository.get_all(page=page, per_page=per_page)

def count():
    return repository.count()


def get_by_id(user_id: int):
    return repository.get_by_id(user_id)                                

def create(user: UserCreate):
    hashed_password = pwd_context.hash(user.hashed_password)
    user_data = UserModel(name=user.name, 
                          email=user.email, 
                          hashed_password=hashed_password)
    return repository.create(user_data) 

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def delete(user_id: int):
    return repository.delete(user_id)

def get_by_email(email: str):
    return repository.get_by_email(email)

def update_password(user_email: EmailStr, hashed_password: str):
    hashed_password = pwd_context.hash(hashed_password)
    return repository.update_password(user_email, hashed_password)


