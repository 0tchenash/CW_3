from project.dao import DirectorDAO
from project.exceptions import ItemNotFound
from project.schemas.directors import DirectorSchema
from project.services.base import BaseService


class DirectorsService(BaseService):
    def get_one(self, director_id):
        director = DirectorDAO(self._db_session).get_one(director_id)
        if not director:
            raise ItemNotFound
        return DirectorSchema().dump(director)

    def get_all(self):
        directors = DirectorDAO(self._db_session).get_all()
        return DirectorSchema(many=True).dump(directors)

    def create(self, data):
        return DirectorDAO(self._db_session).create(data)

    def update(self, data):
        DirectorDAO(self._db_session).update(data)
        return DirectorDAO(self._db_session)

    def delete(self, director_id):
        DirectorDAO(self._db_session).delete(director_id)
