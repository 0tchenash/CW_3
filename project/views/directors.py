from flask import request
from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.tools.container import director_service


directors_ns = Namespace("directors")


@directors_ns.route("/")
class DirectorsView(Resource):
    @directors_ns.response(200, "OK")
    def get(self):
        """Получение всех режиссеров"""
        return director_service.get_all()

    @directors_ns.response(201, "CREATED")
    def post(self):
        data = request.get_json
        director_service.create(data)


@directors_ns.route("/<int:genre_id>")
class DirectorView(Resource):
    @directors_ns.response(200, "OK")
    @directors_ns.response(404, "Director not found")
    def get(self, genre_id: int):
        """Полуние режиссера по айди"""
        try:
            return director_service.get_one(genre_id)
        except ItemNotFound:
            abort(404, message="Director not found")

    @directors_ns.response(200, "OK")
    @directors_ns.response(404, "Director not found")
    def put(self, gid):
        """Изменение режиссера по айди"""
        data = request.get_json()
        data['id'] = gid
        try:
            return director_service.update(data)
        except ItemNotFound:
            abort(404, message="Director not found")

    @directors_ns.response(200, "OK")
    @directors_ns.response(404, "Director not found")
    def delete(self, gid):
        """Удаление режиссера по айди"""
        try:
            return director_service.delete(gid)
        except ItemNotFound:
            abort(404, message="Director not found")
