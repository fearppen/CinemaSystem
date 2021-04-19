from abc import ABC, abstractmethod

from domain import db_session
from domain.user import User


class IUsersRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_user(self, user_id: int):
        pass

    @abstractmethod
    def add(self, user: User):
        pass

    @abstractmethod
    def update(self, user_id: int, new_user: User):
        pass

    @abstractmethod
    def delete(self, user_id: int):
        pass


class UsersRepositorySQLAlchemy(IUsersRepository):
    def get_all(self):
        new_db_session = db_session.create_session()
        return new_db_session.query(User).all()

    def get_user(self, user_id: int):
        new_db_session = db_session.create_session()
        return new_db_session.query(User).filter(User.id == user_id).first()

    def add(self, user: User):
        new_db_session = db_session.create_session()
        new_db_session.add(user)
        new_db_session.commit()

    def update(self, user_id: int, new_user: User):
        new_db_session = db_session.create_session()
        user = new_db_session.query(User).filter(User.id == user_id)
        user.login = new_user.login
        user.password = new_user.password
        user.email = new_user.email
        user.role_id = new_user.role_id
        new_db_session.commit()

    def delete(self, user_id: int):
        new_db_session = db_session.create_session()
        new_db_session.delete(new_db_session.query(User).filter(User.id == user_id))
        new_db_session.commit()
