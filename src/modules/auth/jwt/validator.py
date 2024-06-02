from fastapi import Request, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Callable, List
from functools import wraps
from src.models.users_model import Role, User

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    payload = verify_token(token)
    # Aqui você precisará buscar o usuário no banco de dados
    user = User(email=payload.get("sub"), role=payload.get("role"), name=payload.get("name"))
    if not user:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return user

def jwt_required(func: Callable):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        current_user = kwargs.get('current_user')
        if not current_user:
            raise HTTPException(status_code=400, detail="Current user is missing")
        return await func(*args, **kwargs)
    return wrapper

def permission_required(required_permissions: List[str]):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            current_user = kwargs.get('current_user')
            if not current_user:
                raise HTTPException(status_code=400, detail="Current user is missing")
            if not set(required_permissions).issubset(set([current_user.role])):
                raise HTTPException(status_code=403, detail="Permissões insuficientes")
            return await func(*args, **kwargs)
        return wrapper
    return decorator

def generate_token(user: User):
    return jwt.encode(
        {
            "sub": user.email,
            "role": user.role,
            "name": user.name
        }, SECRET_KEY, algorithm=ALGORITHM)
