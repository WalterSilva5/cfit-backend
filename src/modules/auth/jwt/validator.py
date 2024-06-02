from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Callable
from src.models.users_model import User
from typing import List
from functools import wraps

app = FastAPI()

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


from fastapi import Request, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Callable, List
from functools import wraps
from src.models.users_model import Role
from src.modules.user import service

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str):
    print("verifying token")
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

def jwt_required(func: Callable):
    print("decorator jwt_required")
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request: Request = kwargs.get('request')
        if not request:
            raise HTTPException(status_code=400, detail="Request is missing")
        token: str = await oauth2_scheme(request)
        verify_token(token)
        return await func(*args, **kwargs)
    return wrapper

def permission_required(required_permissions: List[str]):
    print("decorator permission_required - required_permissions: ", required_permissions)
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request: Request = kwargs.get('request')
            if not request:
                raise HTTPException(status_code=400, detail="Request is missing")
            token: str = await oauth2_scheme(request)
            payload = verify_token(token)
            user_permissions = payload.get("role", [])
            if not set(required_permissions).issubset(set(user_permissions)):
                raise HTTPException(status_code=403, detail="Permissões insuficientes")
            return await func(*args, **kwargs)
        return wrapper
    return decorator

def generate_token(user: User):
    """
    Generate a JWT token for a user.

    Args:
        user (User): The user for whom the token is to be generated.

    Returns:
        str: The JWT token.
    """
    return jwt.encode(
        {
        "sub": user.email,
        "role": user.role,
        "name": user.name
        }, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(request: Request) -> User:
    token = request.headers.get("Authorization")
    print("\n\nget_current_user - token: ", token)
    if not token or "Bearer " not in token:
        raise HTTPException(status_code=401, detail="Token não fornecido")
    
    token = token.split("Bearer ")[1]
    payload = verify_token(token)
    
    return User(email=payload.get("sub"), role=payload.get("role"), name=payload.get("name"))
