from project.dao.models import Favorite
from project.setup_db import db


class FavoriteDAO:
    def __init__(self, session):
        self.session = session

    def add_movie(self, movie_id, user):
        data = {
            "movie_id": movie_id,
            "user_id": user.id
        }
        favorite = Favorite(**data)
        db.session.add(favorite)
        db.session.commit()

    def delete(self, movie_id, user):
        movie = self.session.query(Favorite).filter(Favorite.movie_id == movie_id and Favorite.user_id == user.id)
        db.session.delete(movie)
        db.session.commit()
