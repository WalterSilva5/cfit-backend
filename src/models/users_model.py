from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from src.modules.database.db_connection import Base
from enum import Enum

class Role(Enum):
    """
    Enum class for user roles
    """
    ADMIN = 'admin'
    USER = 'user'
    
class User(Base):
    """
    User model class for storing user related details
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    role = Column(String, default=Role.USER.value)