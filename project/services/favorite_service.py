

class FavoriteService:
    def __init__(self, dao):
        self.dao = dao

    def add_movie(self, movie_id, user):
        return self.dao.add_movie(movie_id, user)

    def delete(self, movie_id, user):
        return self.dao.delete(movie_id, user)
