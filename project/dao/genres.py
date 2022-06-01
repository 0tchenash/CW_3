

from project.dao.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, genre_id):
        return self.session.query(Genre).filter(Genre.id == genre_id).one_or_none()

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, genre_id):
        genre = self.get_one(genre_id)
        self.session.delete(genre)
        self.session.commit()

    def update(self, data):
        genre = self.get_one(data.get("id"))
        genre.name = data.get("name")

        self.session.add(genre)
        self.session.commit()
