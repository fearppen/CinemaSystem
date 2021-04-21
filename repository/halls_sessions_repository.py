from abc import ABC, abstractmethod

from domain import db_session
from domain.hall import Hall
from domain.hall_session import hall_session_table
from domain.session import Session


class IHallsSessionsRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_hall_sessions(self, hall_id: int):
        pass

    @abstractmethod
    def add(self, hall: Hall, session: Session):
        pass

    @abstractmethod
    def update(self, hall: Hall, session: Session, new_session: Session):
        pass

    @abstractmethod
    def delete(self, hall: Hall, session: Session):
        pass


class HallsSessionsRepositorySQLAlchemy(IHallsSessionsRepository):
    def get_all(self):
        new_db_session = db_session.create_session()
        return new_db_session.query(hall_session_table).all()

    def get_hall_sessions(self, hall_id: int):
        new_db_session = db_session.create_session()
        return new_db_session.query(hall_session_table).filter(
            hall_session_table.hall_id == hall_id).all()

    def add(self, hall: Hall, session: Session):
        new_db_session = db_session.create_session()
        hall.session.append(session)
        new_db_session.commit()

    def update(self, hall: Hall, session: Session, new_session: Session):
        new_db_session = db_session.create_session()
        hall.session.remove(session)
        hall.session.append(new_session)
        new_db_session.commit()

    def delete(self, hall: Hall, session: Session):
        new_db_session = db_session.create_session()
        hall.session.remove(session)
        new_db_session.commit()
