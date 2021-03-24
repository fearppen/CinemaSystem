from abc import ABC, abstractmethod

from domain import db_session
from domain.film import Film

db_session.global_init("db/system.db")


class IFilmsRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_film(self, film_id: int):
        pass

    @abstractmethod
    def add(self, film: Film):
        pass

    @abstractmethod
    def update(self, film_id: int, new_film: Film):
        pass

    @abstractmethod
    def delete(self, film_id: int):
        pass


class FilmsRepositorySQLAlchemy(IFilmsRepository):
    def get_all(self):
        session = db_session.create_session()
        return session.query(Film).all()

    def get_film(self, film_id: int):
        session = db_session.create_session()
        return session.query(Film).filter(Film.id == film_id)

    def add(self, film: Film):
        session = db_session.create_session()
        session.add(film)
        session.commit()

    def update(self, film_id: int, new_film: Film):
        session = db_session.create_session()
        film = session.query(Film).filter(Film.id == film_id)
        film.title = new_film.title
        film.release_date = new_film.release_date
        film.duration = new_film.duration
        film.director = new_film.director
        film.genre_id = new_film.genre_id
        session.commit()

    def delete(self, film_id: int):
        session = db_session.create_session()
        session.delete(session.query(Film).filter(Film.id == film_id))
        session.commit()
