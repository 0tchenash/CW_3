import base64
import hashlib
import hmac
from project.dao import UserDAO
from project.config import BaseConfig
from project.exceptions import ItemNotFound
from project.schemas.users import UserSchema
from project.services.base import BaseService


class UserService(BaseService):

    def get_all(self):
        users = UserDAO(self._db_session).get_all()
        return UserSchema(many=True).dump(users)

    def get_by_username(self, name):
        user = UserDAO(self._db_session).get_by_username(name)
        if not user:
            raise ItemNotFound
        return UserSchema().dump(user)

    def create(self, data):
        data['password'] = self.generete_password(data['password'])
        return UserDAO(self._db_session).create(data)

    def delete(self, user_id):
        return UserDAO(self._db_session).delete(user_id)

    def generete_password(self, password):
        """хэширование пароля"""
        hash_pass = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            BaseConfig.PWD_HASH_SALT,
            BaseConfig.PWD_HASH_ITERATIONS)
        return base64.b64encode(hash_pass)

    def compare_password(self, hash_password, password):
        """Проверка пароля"""
        decoded_password = base64.b64decode(hash_password)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            BaseConfig.PWD_HASH_SALT,
            BaseConfig.PWD_HASH_ITERATIONS)

        return hmac.compare_digest(decoded_password, hash_digest)
