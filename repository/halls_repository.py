from abc import ABC, abstractmethod

from domain import db_session
from domain.hall import Hall


class IHallsRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_hall(self, hall_id: int):
        pass

    @abstractmethod
    def add(self, hall: Hall):
        pass

    @abstractmethod
    def update(self, hall_id: int, new_hall: Hall):
        pass

    @abstractmethod
    def delete(self, hall_id: int):
        pass


class HallsRepositorySQLAlchemy(IHallsRepository):
    def get_all(self):
        new_db_session = db_session.create_session()
        return new_db_session.query(Hall).all()

    def get_hall(self, hall_id: int):
        new_db_session = db_session.create_session()
        return new_db_session.query(Hall).filter(Hall.id == hall_id)

    def add(self, hall: Hall):
        new_db_session = db_session.create_session()
        new_db_session.add(hall)
        new_db_session.commit()

    def update(self, hall_id: int, new_hall: Hall):
        new_db_session = db_session.create_session()
        hall = new_db_session.query(Hall).filter(Hall.id == hall_id)
        hall.title = new_hall.title
        hall.cinema_id = new_hall.cinema_id
        new_db_session.commit()

    def delete(self, hall_id: int):
        new_db_session = db_session.create_session()
        new_db_session.delete(new_db_session.query(Hall).filter(Hall.id == hall_id))
        new_db_session.commit()
