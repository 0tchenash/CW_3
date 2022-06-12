from flask import request
from flask_restx import Resource, Namespace, abort
from project.exceptions import ItemNotFound
from project.schemas.users import UserSchema

from project.tools.container import user_service, auth_service
from project.tools.decorators import auth_required, admin_required

users_ns = Namespace('users')
user_ns = Namespace('user')


@users_ns.route('/')
class UsersView(Resource):
    @admin_required
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
            return UserSchema().dump(user)
        except ItemNotFound:
            abort(404, message="User not found")

    @auth_required
    @user_ns.response(200, "OK")
    @user_ns.response(404, "User not found")
    def patch(self):
        data = request.json
        token = auth_service.get_token()
        try:
            return user_service.update(data, token)
        except ItemNotFound:
            abort(404, message="User not found")


@user_ns.route('/password')
class UserView(Resource):
    @user_ns.response(201, "OK")
    @user_ns.response(404, "User not found")
    @auth_required
    def put(self):
        try:
            data = request.get_json()
            token = auth_service.get_token()
            user_service.change_password(data, token)
            return "Пароль изменен", 201
        except ItemNotFound:
            abort(404, message="User not found")


@user_ns.route('/delete/<int:uid>')
class UserDelete(Resource):
    @admin_required
    @user_ns.response(200, "OK")
    @user_ns.response(404, "User not found")
    def delete(self, user_id):
        """Удаление пользователя только для (admin)"""
        try:
            return user_service.delete(user_id)
        except ItemNotFound:
            abort(404, message="User not found")
