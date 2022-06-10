

from project.dao.models import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Получение всех пользователей"""
        return self.session.query(User).all()

    def get_one(self, user_id):
        """Получение одного пользователя по айди"""
        return self.session.query(User).get(user_id)

    def create(self, data):
        """Регистрация пользователя"""
        user = User(**data)

        self.session.add(user)
        self.session.commit()

        return user

    def update(self, data, token):
        user = self.get_one(data.get("id"))
        user.name = data.get("name")
        user.surname = data.get("surname")
        user.favorite_genre = data.get("favorite_genre")

    def delete(self, user_id):
        """Удаление пользователя"""
        user = self.session.query(User).get(user_id)

        self.session.delete(user)
        self.session.commit()

    def get_by_useremail(self, email):
        """Получение определенного пользователя с его данными"""
        return self.session.query(User).filter(User.email == email).first()

    def update_password(self, email, new_password):
        user = self.session.query(User).filter(User.email == email).first()
        user.password = new_password
        self.session.commit()
