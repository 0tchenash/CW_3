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
