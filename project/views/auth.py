from flask import request

from flask_restx import Namespace, Resource
from project.tools.container import auth_service, user_service


auth_ns = Namespace("auth")


@auth_ns.route('/register/')
class AuthsView(Resource):
    @auth_ns.response(201, "CREATED")
    def post(self):
        """регистрация пользователя"""
        data = request.get_json()
        user_service.create(data)


@auth_ns.route('/login/')
class AuthsView(Resource):
    def post(self):
        """Получение токена по данным пользователя"""
        data = request.get_json()
        email = data.get('email', None)
        password = data.get('password', None)
        if None in [email, password]:
            return "", 400

        token = auth_service.generate_token(email, password)
        return token

    def put(self):
        """Запрос на обновление токена с помощью 'refresh_token'"""
        data = request.get_json()
        token = data.get('refresh_token')

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201
