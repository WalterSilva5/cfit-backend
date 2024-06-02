from src.modules.database.db_connection import SessionLocal
from src.models.users_model import User as UserModel
from src.modules.user.service import pwd_context
from src.models.users_model import Role
def seed():
    session = SessionLocal()
    user = UserModel(
        name="admin",
        email="admin@admin.com",
        hashed_password=pwd_context.hash("admin"),
        role=Role.ADMIN.value
    )
    
    session.add(user)
    session.commit()
    session.close()
    
    print("Seeded admin user")
    
if __name__ == "__main__":
    seed()