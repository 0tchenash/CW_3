from project.dao import DirectorDAO
from project.dao import GenreDAO
from project.dao import MovieDAO
from project.dao import UserDAO
from project.dao import FavoriteDAO
from project.services import DirectorsService, favorite_service
from project.services import GenresService
from project.services import MovieService
from project.services import UserService
from project.services import AuthService
from project.services import FavoriteService
from project.setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)
favorite_dao = FavoriteDAO(session=db.session)

director_service = DirectorsService(dao=director_dao)
genre_service = GenresService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
favorite_service = FavoriteService(dao=favorite_dao)

auth_service = AuthService(UserService(user_dao))
