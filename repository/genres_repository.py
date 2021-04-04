from abc import ABC, abstractmethod

from domain import db_session
from domain.genre import Genre


class IGenresRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_genre(self, genre_id: Genre):
        pass


class GenresRepositorySQLAlchemy(IGenresRepository):
    def get_all(self):
        new_db_session = db_session.create_session()
        return new_db_session.query(Genre).all()

    def get_genre(self, genre_id: Genre):
        new_db_session = db_session.create_session()
        return new_db_session.query(Genre).filter(Genre.id == genre_id)
