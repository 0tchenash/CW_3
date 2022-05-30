from flask import request

from flask_restx import Namespace, Resource
from project.services import AuthService, UserService
from project.setup_db import db

auth_ns = Namespace("auth")


@auth_ns.route('/register/')
class AuthsView(Resource):

    def post(self):
        """регистрация пользователя"""
        data = request.get_json()
        UserService(db.session).create(data)


@auth_ns.route('/login/')
class AuthsView(Resource):
    def post(self):
        """Получение токена по данным пользователя"""
        data = request.get_json()
        email = data.get('email', None)
        password = data.get('password', None)
        if None in [email, password]:
            return "", 400

        token = AuthService(db.session).generate_token(email, password)
        return token

    def put(self):
        """Запрос на обновление токена с помощью 'refresh_token'"""
        data = request.get_json()
        token = data.get('refresh_token')

        tokens = AuthService(db.session).approve_refresh_token(token)

        return tokens, 201
