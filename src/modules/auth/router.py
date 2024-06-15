from fastapi import APIRouter, HTTPException, Body
from src.modules.auth.dto import UserAuth
from src.modules.auth.service import auth_user
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends


router = APIRouter()

payload_example = {"email": "admin@admin.com", "password": "admin"}

@router.post(
    "/auth",
    tags=["Auth"], response_model=dict,
    description="Authenticate user and return JWT token",
    )
async def authenticate_user(user_auth: UserAuth = Body(
    ..., examples = [
        payload_example
    ])):

    token = auth_user(user_auth)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"authToken": token}
