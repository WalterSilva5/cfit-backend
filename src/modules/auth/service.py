from src.modules.auth.dto import UserAuth
from src.modules.auth.jwt.validator import create_access_token
from src.modules.user.service import (
    get_by_email,
    pwd_context,
    verify_password)


def auth_user(user_data: UserAuth):
    user = get_by_email(user_data.email)
    if not user:
        return None
    if not verify_password(user_data.password, user.hashed_password):
        return None
    del user.hashed_password
    user_dict = {
        "email": user.email,
        "role": user.role,
        "name": user.name
    }
    token = create_access_token(user_dict)
    return token

