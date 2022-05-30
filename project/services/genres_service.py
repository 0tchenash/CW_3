from project.dao import GenreDAO
from project.exceptions import ItemNotFound
from project.schemas.genres import GenreSchema
from project.services.base import BaseService


class GenresService(BaseService):
    def get_one(self, genre_id):
        genre = GenreDAO(self._db_session).get_one(genre_id)
        if not genre:
            raise ItemNotFound
        return GenreSchema().dump(genre)

    def get_all(self):
        genres = GenreDAO(self._db_session).get_all()
        return GenreSchema(many=True).dump(genres)

    def create(self, data):
        return GenreDAO(self._db_session).create(data)

    def update(self, data):
        GenreDAO(self._db_session).update(data)
        return GenreDAO(self._db_session)

    def delete(self, genre_id):
        GenreDAO(self._db_session).delete(genre_id)
