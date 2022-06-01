from flask import request
from flask_restx import Resource, Namespace, abort
from project.exceptions import ItemNotFound

from project.tools.container import movie_service
from project.tools.decorators import auth_required

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    @auth_required
    @movies_ns.response(200, "OK")
    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        page = request.args.get('page')
        status = request.args.get('status')
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        return movie_service.get_all(filters, page, status)

    @movies_ns.response(201, "CREATED")
    def post(self):
        data = request.json
        movie_service.create(data)


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):
    @movies_ns.response(200, "OK")
    @movies_ns.response(404, "Movie not found")
    def get(self, movie_id):
        try:
            return movie_service.get_one(movie_id)
        except ItemNotFound:
            abort(404, message="Movie not found")

    @movies_ns.response(200, "OK")
    @movies_ns.response(404, "Movie not found")
    def put(self, movie_id):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = movie_id
        try:
            return movie_service.update(req_json)
        except ItemNotFound:
            abort(404, message="Movie not found")

    @movies_ns.response(200, "OK")
    @movies_ns.response(404, "Movie not found")
    def delete(self, movie_id):
        try:
            return movie_service.update(movie_id)
        except ItemNotFound:
            abort(404, message="Movie not found")
