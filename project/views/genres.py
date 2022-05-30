from flask import request
from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.services import GenresService
from project.setup_db import db

genres_ns = Namespace("genres")


@genres_ns.route("/")
class GenresView(Resource):
    @genres_ns.response(200, "OK")
    def get(self):
        """Get all genres"""
        return GenresService(db.session).get_all()

    @genres_ns.response(201, "CREATED")
    def post(self):
        data = request.get_json
        GenresService(db.session).create(data)


@genres_ns.route("/<int:genre_id>")
class GenreView(Resource):
    @genres_ns.response(200, "OK")
    @genres_ns.response(404, "Genre not found")
    def get(self, genre_id: int):
        """Get genre by id"""
        try:
            return GenresService(db.session).get_one(genre_id)
        except ItemNotFound:
            abort(404, message="Genre not found")

    @genres_ns.response(200, "OK")
    @genres_ns.response(404, "Genre not found")
    def put(self, gid):
        data = request.get_json()
        data['id'] = gid
        try:
            return GenresService(db.session).update(data)
        except ItemNotFound:
            abort(404, message="Genre not found")

    @genres_ns.response(200, "OK")
    @genres_ns.response(404, "Genre not found")
    def delete(self, gid):
        try:
            return GenresService(db.session).delete(gid)
        except ItemNotFound:
            abort(404, message="Genre not found")

