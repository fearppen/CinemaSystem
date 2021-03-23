from abc import ABC, abstractmethod

from domain import db_session
from domain.genre import Genre

db_session.global_init("db/system.db")


class IGenreRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass


class GenreRepositorySQLAlchemy(IGenreRepository):
    def get_all(self):
        session = db_session.create_session()
        return session.query(Genre).all()
