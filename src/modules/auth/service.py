from src.modules.auth.dto import UserAuth
from src.modules.auth.jwt.validator import generate_token, verify_token
from src.modules.user.service import (
    get_user_by_email,
    pwd_context,
    verify_password)


def auth_user(user_data: UserAuth):
    user = get_user_by_email(user_data.email)
    if not user:
        return None
    if not verify_password(user_data.password, user.hashed_password):
        return None
    token = generate_token(user)
    return token


def verify_user(token: str):
    return verify_token(token)
