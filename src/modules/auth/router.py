from fastapi import APIRouter, HTTPException, Depends
from src.modules.auth.dto import UserAuth
from src.modules.auth.service import auth_user

router = APIRouter()

@router.post("/auth", tags=["Auth"], response_model=dict)
async def authenticate_user(user_auth: UserAuth):
    token = auth_user(user_auth)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"authToken": token}
