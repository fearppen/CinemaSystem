from abc import ABC, abstractmethod

from domain import db_session
from domain.cinema import Cinema


class ICinemasRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_cinema(self, cinema_id: int):
        pass

    @abstractmethod
    def add(self, cinema: Cinema):
        pass

    @abstractmethod
    def update(self, cinema_id: int, new_cinema: Cinema):
        pass

    @abstractmethod
    def delete(self, cinema_id: int):
        pass


class CinemasRepositorySQLAlchemy(ICinemasRepository):
    def get_all(self):
        new_db_session = db_session.create_session()
        return new_db_session.query(Cinema).all()

    def get_cinema(self, cinema_id: int):
        new_db_session = db_session.create_session()
        return new_db_session.query(Cinema).filter(Cinema.id == cinema_id).first()

    def add(self, cinema: Cinema):
        new_db_session = db_session.create_session()
        new_db_session.add(cinema)
        new_db_session.commit()

    def update(self, cinema_id: int, new_cinema: Cinema):
        new_db_session = db_session.create_session()
        cinema = new_db_session.query(Cinema).filter(Cinema.id == cinema_id)
        cinema.title = new_cinema.title
        new_db_session.commit()

    def delete(self, cinema_id: int):
        new_db_session = db_session.create_session()
        new_db_session.delete(new_db_session.query(Cinema).filter(Cinema.id == cinema_id))
        new_db_session.commit()
