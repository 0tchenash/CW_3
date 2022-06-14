from project.setup_db import db


class Favorite(db.Model):
    __tablename__ = 'favorite'
    idx = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    movie = db.relationship("Movie")
    user = db.relationship("User")
