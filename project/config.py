import base64
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = "you-will-never-guess"
    JWT_ALGORITHM = "HS256"
    JSON_AS_ASCII = False

    ITEMS_PER_PAGE = 12

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 130

    PWD_HASH_SALT = base64.b64decode("salt")
    PWD_HASH_ITERATIONS = 100_000


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"


class DevelopmentConfig(BaseConfig):
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"

class Constants():
    ALLOWED_DOMENS = ['gmail.com', 'mail.ru', 'bk.ru', 'yandex.ru', 'icloud.com', 'skypro.ru', 'inbox.ru']
    UNALLOWED_PASSWORDS = ['1234', 'qwer', '1111', '0000']
