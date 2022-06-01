from flask import request
from flask_restx import Resource, Namespace, abort
from project.exceptions import ItemNotFound

from project.tools.container import user_service


users_ns = Namespace('users')


@users_ns.route('/')
class UsersView(Resource):
    @users_ns.response(200, "OK")
    def get(self):
        """Получение всех зарегистрированных пользователей"""
        return user_service.get_all()

    @users_ns.response(201, "CREATED")
    def post(self):
        """Регистрация нового пользователя"""
        data = request.get_json()
        user_service.create(data)



@users_ns.route('/<int:user_id>')
class UserView(Resource):
    @users_ns.response(200, "OK")
    @users_ns.response(404, "Movie not found")
    def get(self, user_id):
        try:
            return user_service.get_one(user_id)
        except ItemNotFound:
            abort(404, message="Movie not found")

    def patch(self, user_id):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = user_id
        try:
            return user_service.update(req_json)
        except ItemNotFound:
            abort(404, message="Movie not found")

    @users_ns.response(200, "OK")
    @users_ns.response(404, "Movie not found")
    def delete(self, user_id):
        """Удаление пользователя только для (admin)"""
        try:
            return user_service.delete(user_id)
        except ItemNotFound:
            abort(404, message="Movie not found")
