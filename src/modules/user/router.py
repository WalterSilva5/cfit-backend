from src.modules.auth.dto import UserAuth
from src.modules.user.dto import UserCreate, User, UserLogin
from typing import Any
from fastapi import HTTPException, APIRouter, Depends
from src.modules.user import service
from fastapi.security import HTTPAuthorizationCredentials
from src.modules.auth.jwt.validator import security
from src.utils.dtos.pagination_dto import Paginated
from src.utils.pagination.get_meta import get_meta
from typing import Any
from fastapi import Query
from src.modules.user import service
from src.modules.auth import service as service_auth
from src.modules.user.dto import UpdatePasswordRequest


BASE_URL = "/users"
CONTEXT = "User"
router = APIRouter()

@router.get(BASE_URL, response_model=Paginated[User], tags=[CONTEXT])
async def get_all(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    page: int = Query(1, gt=0),
    per_page: int = Query(10, gt=0)
):
    try:
        users = service.get_all(page=page, per_page=per_page)
        total_users = service.count()
        last_page = total_users // per_page + (total_users % per_page > 0)
        meta = get_meta(total_users, last_page, page, per_page)
        return Paginated(data=users, meta=meta)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get(BASE_URL + "/{user_id}", response_model=User, tags=[CONTEXT])
async def get_by_id(user_id: int,
                         credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        user = service.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error getting user")

@router.post(BASE_URL, response_model=User, tags=[CONTEXT])
async def create(user: UserCreate):
    try:
        return service.create(user)
    except Exception as e:
        message = "Error creating user"
        if "UNIQUE" in str(e):
            message = "Username already exists"
        raise HTTPException(
            status_code=400, detail=message
        )
        
@router.delete(BASE_URL + "/{user_id}", tags=[CONTEXT])
async def delete(user_id: int,
                      credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        service.delete(user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str("Error deleting user"))    
    
@router.post(BASE_URL + "/auth/login", tags=[CONTEXT])
async def login(user_data: UserAuth):
    token = service_auth.auth_user(user_data)
    if not token:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"token": token}
    

@router.put(BASE_URL + "/alter/password", tags=[CONTEXT])
async def update_password_user(user: UpdatePasswordRequest):
    try:
        return service.update_password(user.email, user.hashed_password)
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found")
    
