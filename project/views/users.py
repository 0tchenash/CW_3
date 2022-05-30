from flask import request
from flask_restx import Resource, Namespace, abort
from project.exceptions import ItemNotFound

from project.services import UserService
from project.setup_db import db

users_ns = Namespace('users')


@users_ns.route('/')
class UsersView(Resource):
    @users_ns.response(200, "OK")
    def get(self):
        """Получение всех зарегистрированных пользователей"""
        return UserService(db.session).get_all()

    @users_ns.response(201, "CREATED")
    def post(self):
        """Регистрация нового пользователя"""
        data = request.get_json()
        UserService(db.session).create(data)



@users_ns.route('/<int:user_id>')
class UserView(Resource):
    @users_ns.response(200, "OK")
    @users_ns.response(404, "Movie not found")
    def delete(self, user_id):
        """Удаление пользователя только для (admin)"""
        try:
            return UserService(db.session).delete(user_id)
        except ItemNotFound:
            abort(404, message="Movie not found")
