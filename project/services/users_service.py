import base64
import hashlib
import hmac
from project.dao import UserDAO
from project.config import BaseConfig
from project.exceptions import ItemNotFound
from project.schemas.users import UserSchema


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        users = self.dao.get_all()
        return UserSchema(many=True).dump(users)

    def get_one(self, user_id):
        user = self.dao.get_one(user_id)
        return UserSchema().dump(user)

    def get_by_useremail(self, email):
        user = self.dao.get_by_useremail(email)
        if not user:
            raise ItemNotFound
        return UserSchema().dump(user)

    def create(self, data):
        data['password'] = self.generate_password(data['password'])
        return self.dao.create(data)

    def update(self, data):
        self.dao.update(data)

    def delete(self, user_id):
        return self.dao.delete(user_id)

    def generate_password(self, password):
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

    def change_password(self, data, token):
        new_password = self.generate_password(data["new_password"])
        password = data['password']
        email = token['email']

        if self.compare_password(token["password"], password):
            return self.dao.update_password(email, new_password)

