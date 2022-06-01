from flask import request
from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.tools.container import genre_service


genres_ns = Namespace("genres")


@genres_ns.route("/")
class GenresView(Resource):
    @genres_ns.response(200, "OK")
    def get(self):
        """Get all genres"""
        return genre_service.get_all()

    @genres_ns.response(201, "CREATED")
    def post(self):
        data = request.get_json
        genre_service.create(data)


@genres_ns.route("/<int:genre_id>")
class GenreView(Resource):
    @genres_ns.response(200, "OK")
    @genres_ns.response(404, "Genre not found")
    def get(self, genre_id: int):
        """Get genre by id"""
        try:
            return genre_service.get_one(genre_id)
        except ItemNotFound:
            abort(404, message="Genre not found")

    @genres_ns.response(200, "OK")
    @genres_ns.response(404, "Genre not found")
    def put(self, gid):
        data = request.get_json()
        data['id'] = gid
        try:
            return genre_service.update(data)
        except ItemNotFound:
            abort(404, message="Genre not found")

    @genres_ns.response(200, "OK")
    @genres_ns.response(404, "Genre not found")
    def delete(self, gid):
        try:
            return genre_service.delete(gid)
        except ItemNotFound:
            abort(404, message="Genre not found")

