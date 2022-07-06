from flask import Flask, render_template
from flask_restx import Api

from project.config import DevelopmentConfig
from project.setup_db import db

from project.views.auth import auth_ns
from project.views.directors import directors_ns
from project.views.favorite import favorite_ns
from project.views.genres import genres_ns
from project.views.movies import movies_ns
from project.views.users import user_ns


def register_extensions(app):
    db.init_app(app)
    api = Api(app, title="Flask Course Project 4", doc="/docs")
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(favorite_ns)


app = Flask(__name__)
app.config.from_object(DevelopmentConfig())


@app.route('/')
def index():
    return render_template('index.html')


register_extensions(app)

if __name__ == '__main__':
    app.run(port=25000)
