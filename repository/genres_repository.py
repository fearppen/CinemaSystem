from abc import ABC, abstractmethod

from domain import db_session
from domain.genre import Genre


class IGenresRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass


class GenresRepositorySQLAlchemy(IGenresRepository):
    def get_all(self):
        new_db_session = db_session.create_session()
        return new_db_session.query(Genre).all()
