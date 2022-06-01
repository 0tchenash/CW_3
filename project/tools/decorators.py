import jwt

from flask import request, abort
from project.config import BaseConfig

def auth_required(func):
    """проверка зарегестрированного пользователя"""
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.JWT_ALGORITHM])
        except Exception as e:
            print('JWT Decode Exception', e)
            abort(401)
        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    """проверка прав пользователя"""
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        role = None
        try:
            user = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.JWT_ALGORITHM])
            role = user.get("role", "user")
        except Exception as e:
            print('JWT Decode Exception', e)
            abort(401)

        if role != "admin":
            abort(403)
        return func(*args, **kwargs)
    return wrapper