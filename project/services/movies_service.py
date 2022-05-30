from project.dao import MovieDAO
from project.exceptions import ItemNotFound
from project.schemas.movies import MovieSchema
from project.services.base import BaseService


class MovieService(BaseService):

    def get_one(self, movie_id):
        movie = MovieDAO(self._db_session).get_one(movie_id)
        if not movie:
            raise ItemNotFound
        return MovieSchema().dump(movie)

    def get_all(self, filters):
        if filters.get("director_id") is not None:
            movies = MovieDAO(self._db_session).get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = MovieDAO(self._db_session).get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = MovieDAO(self._db_session).get_by_year(filters.get("year"))
        else:
            movies = MovieDAO(self._db_session).get_all()
        return MovieSchema(many=True).dump(movies)

    def create(self, data):
        return MovieDAO(self._db_session).create(data)

    def update(self, data):
        MovieDAO(self._db_session).update(data)
        return MovieDAO(self._db_session)

    def delete(self, movie_id):
        MovieDAO(self._db_session).delete(movie_id)
