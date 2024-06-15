from pydantic import EmailStr
from src.modules.database.db_connection import SessionLocal
from src.models.users_model import User as UserModel
from src.modules.user.dto import User

def get_all(page: int = 1, per_page: int = 10):
    session = SessionLocal()
    data = session.query(UserModel).offset((page - 1) * per_page).limit(per_page).all()
    data = [
        generate_user_instance(user) for user in data
    ]
    session.close()
    return data

def count():
    session = SessionLocal()
    total_users = session.query(UserModel).count()
    session.close()
    return total_users

def generate_user_instance(user: UserModel) -> User:
    return User(id=user.id, 
                name=user.name,
                email=user.email,
                is_active=user.is_active,
                created_at=user.created_at,
                updated_at=user.updated_at,
                role=user.role,
                )

def get_by_id(user_id: int):
    session = SessionLocal()
    user = session.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        data = generate_user_instance(user)
    else:
        data = None
    session.close()
    return data

def create(user):
    session = SessionLocal()
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()
    del user.hashed_password
    return user


def delete(user_id: int):
    session = SessionLocal()
    user = session.query(UserModel).filter(UserModel.id == user_id).first()
    session.delete(user)
    session.commit()
    session.close()
    return user
    
def get_by_email(email: str):
    session = SessionLocal()
    user = session.query(UserModel).filter(UserModel.email == email).first()
    if user:
        data = user
    else:
        data = None
    session.close()
    return data

def update_password(user_email: EmailStr, hashed_password: str):
    session = SessionLocal()
    user = session.query(UserModel).filter(UserModel.email == user_email).first()
    user.hashed_password = hashed_password
    session.commit()
    session.close()
    return user
