

from project.dao.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, movie_id):
        return self.session.query(Movie).get(movie_id)

    def get_all_page(self, lim, offs):
        return self.session.query(Movie).limit(lim).offset(offs).all()

    def get_all(self):
        return self.session.query(Movie).all()


    def get_by_director_id(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_by_genre_id(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, movie_id):
        movie = self.get_one(movie_id)
        self.session.delete(movie)
        self.session.commit()

    def update(self, data):
        movie = self.get_one(data.get("id"))
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.session.add(movie)
        self.session.commit()

    def get_all_sorted_asc(self):
        return self.session.query(Movie).order_by(Movie.year.asc()).all()

    def get_all_sorted_desc(self):
        return self.session.query(Movie).order_by(Movie.year.desc()).all()
