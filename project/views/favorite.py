from flask import request
from flask_restx import Resource, Namespace, abort
from project.exceptions import ItemNotFound

from project.tools.container import favorite_service, auth_service, user_service
from project.tools.decorators import auth_required

favorite_ns = Namespace('favorite')


@favorite_ns.route('/<int:mid>')
class FavoriteView(Resource):
    @auth_required
    def post(self, mid):
        data = auth_service.get_token()
        user = user_service.get_by_useremail(data['email'])
        favorite_service.add_movie(mid, user)
        return "Фильм добавлен в избранное!", 200

    @auth_required
    def delete(self, mid):
        data = auth_service.get_token()
        user = user_service.get_by_useremail(data['email'])
        favorite_service.delete(mid, user)
        return "Фильм удален из избранного!", 204

