import datetime
import calendar
import jwt

from flask_restx import abort
from project.config import BaseConfig
from project.services import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_token(self, email, password, is_refresh=False):
        """Создание токена на основе данных пользователя"""
        user = self.user_service.get_by_useremail(email)
        print(user)
        if user is None:
            raise abort(404)

        # if not self.user_service.compare_password(user.password, password):
        #     abort(400)

        data = {
            'name': user['name'],
            'role': user['role']
        }

        # Выдача токена на определенное время
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, BaseConfig.SECRET_KEY, BaseConfig.JWT_ALGORITHM)
        #
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, BaseConfig.SECRET_KEY, BaseConfig.JWT_ALGORITHM)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        """Обновление токена с помощью (refresh_token)"""
        data = jwt.decode(jwt=refresh_token, key=BaseConfig.SECRET_KEY, algorithms=BaseConfig.JWT_ALGORITHM)
        email = data.get('email')

        return self.generate_token(email, None)
