from project.dao import MovieDAO
from project.exceptions import ItemNotFound
from project.schemas.movies import MovieSchema
from project.services.base import BaseService


class MovieService:
    def __init__(self, dao):
        self.dao = dao

    def get_one(self, movie_id):
        movie = self.dao.get_one(movie_id)
        if not movie:
            raise ItemNotFound
        return MovieSchema().dump(movie)

    def get_all(self, filters, page, status):
        if status is not None:
            if status == 'new':
                movies = self.dao.get_all_sorted_desc()
            if status == 'old':
                movies = self.dao.get_all_sorted_asc()
        elif page is not None:
            lim = 12
            offs = (int(page) - 1) * lim
            movies = self.dao.get_all_page(lim, offs)
        elif filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()
        return MovieSchema(many=True).dump(movies)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        self.dao.update(data)


    def delete(self, movie_id):
        self.dao.delete(movie_id)
