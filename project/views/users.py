from flask import request
from flask_restx import Resource, Namespace, abort
from project.exceptions import ItemNotFound

from project.tools.container import user_service, auth_service
from project.tools.decorators import auth_required, admin_required

users_ns = Namespace('users')
user_ns = Namespace('user')


@users_ns.route('/')
class UsersView(Resource):
    @users_ns.response(200, "OK")
    def get(self):
        """Получение всех зарегистрированных пользователей"""
        return user_service.get_all()


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    @user_ns.response(200, "OK")
    @user_ns.response(404, "User not found")
    def get(self):
        try:
            data = auth_service.get_token()
            user = user_service.get_by_useremail(data['email'])
            return user
        except ItemNotFound:
            abort(404, message="User not found")

    @user_ns.response(200, "OK")
    @user_ns.response(404, "User not found")
    def patch(self, user_id):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = user_id
        try:
            return user_service.update(req_json)
        except ItemNotFound:
            abort(404, message="User not found")


@user_ns.route('/password')
class UserView(Resource):
    @user_ns.response(201, "OK")
    @user_ns.response(404, "User not found")
    @auth_required
    def put(self):
        data = request.get_json()
        token = auth_service.get_token()
        user_service.change_password(data, token)
        return "Пароль изменен", 201

    @user_ns.response(200, "OK")
    @user_ns.response(404, "User not found")
    def delete(self, user_id):
        """Удаление пользователя только для (admin)"""
        try:
            return user_service.delete(user_id)
        except ItemNotFound:
            abort(404, message="User not found")
