from flask import Flask
# from flask_cors import CORS
from flask_restx import Api

from project.config import DevelopmentConfig, BaseConfig
from project.setup_db import db
from project.views import genres_ns, movies_ns, directors_ns, users_ns, auth_ns
from project.views.favorite import favorite_ns
from project.views.users import user_ns

api = Api(
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    title="Flask Course Project 3",
    doc="/docs",
)

# Нужно для работы с фронтендом
# cors = CORS()


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    # cors.init_app(app)
    db.init_app(app)
    #api.init_app(app)
    api = Api(app)

    # Регистрация эндпоинтов
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(users_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(favorite_ns)

    return app


if __name__ == '__main__':
    app = create_app(DevelopmentConfig())
    app.run(debug=True, port=10331)
