from project.dao import GenreDAO
from project.exceptions import ItemNotFound
from project.schemas.genres import GenreSchema
from project.services.base import BaseService


class GenresService:
    def __init__(self, dao):
        self.dao = dao

    def get_one(self, genre_id):
        genre = self.dao.get_one(genre_id)
        if not genre:
            raise ItemNotFound
        return GenreSchema().dump(genre)

    def get_all(self):
        genres = self.dao.get_all()
        return GenreSchema(many=True).dump(genres)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        self.dao.update(data)


    def delete(self, genre_id):
        self.dao.delete(genre_id)
