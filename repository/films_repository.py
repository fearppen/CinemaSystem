from abc import ABC, abstractmethod

from domain import db_session
from domain.film import Film


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
        new_db_session = db_session.create_session()
        return new_db_session.query(Film).all()

    def get_film(self, film_id: int):
        new_db_session = db_session.create_session()
        return new_db_session.query(Film).filter(Film.id == film_id)

    def add(self, film: Film):
        new_db_session = db_session.create_session()
        new_db_session.add(film)
        new_db_session.commit()

    def update(self, film_id: int, new_film: Film):
        new_db_session = db_session.create_session()
        film = new_db_session.query(Film).filter(Film.id == film_id)
        film.title = new_film.title
        film.release_date = new_film.release_date
        film.duration = new_film.duration
        film.director = new_film.director
        film.genre_id = new_film.genre_id
        new_db_session.commit()

    def delete(self, film_id: int):
        new_db_session = db_session.create_session()
        new_db_session.delete(new_db_session.query(Film).filter(Film.id == film_id))
        new_db_session.commit()
