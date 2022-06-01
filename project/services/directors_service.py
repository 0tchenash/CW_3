from project.dao import DirectorDAO
from project.exceptions import ItemNotFound
from project.schemas.directors import DirectorSchema
from project.services.base import BaseService


class DirectorsService:
    def __init__(self, dao):
        self.dao = dao

    def get_one(self, director_id):
        director = self.dao.get_one(director_id)
        if not director:
            raise ItemNotFound
        return DirectorSchema().dump(director)

    def get_all(self):
        directors = self.dao.get_all()
        return DirectorSchema(many=True).dump(directors)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        self.dao.update(data)


    def delete(self, director_id):
        self.dao.delete(director_id)
