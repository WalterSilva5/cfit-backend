from src.modules.user.dto import UserCreate, User
from typing import Any
from fastapi import HTTPException, APIRouter
from src.modules.user import  service
from typing import List
from src.modules.auth.jwt.validator import jwt_required, permission_required, get_current_user
from src.models.users_model import Role
from fastapi import Depends

BASE_URL = "/users"
CONTEXT = "User"
router = APIRouter()

@router.get("/users", response_model=List[User], tags=["User"])
@jwt_required
@permission_required([Role.ADMIN.value])
async def get_all_users(current_user: User = Depends(get_current_user)):
    try:
        return service.get_all_users()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.get(BASE_URL + "/{user_id}", response_model=User, tags=[CONTEXT])
async def get_user_by_id(user_id: int):
    try:
        user = service.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error getting user")

@router.post(BASE_URL, response_model=User, tags=[CONTEXT])
async def create_user(user: UserCreate):
    try:
        return service.create_user(user)
    except Exception as e:
        message = "Error creating user"
        if "UNIQUE" in str(e):
            message = "Username already exists"
        raise HTTPException(
            status_code=400, detail=message
        )
        
@router.delete(BASE_URL + "/{user_id}", tags=[CONTEXT])
async def delete_user(user_id: int):
    try:
        service.delete_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str("Error deleting user"))
