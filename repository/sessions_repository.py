from abc import ABC, abstractmethod

from domain import db_session
from domain.session import Session


class ISessionsRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_session(self, session_id: int):
        pass

    @abstractmethod
    def add(self, session: Session):
        pass

    @abstractmethod
    def update(self, session_id: int, new_session: Session):
        pass

    @abstractmethod
    def delete(self, session_id: int):
        pass


class FilmsRepositorySQLAlchemy(ISessionsRepository):
    def get_all(self):
        new_db_session = db_session.create_session()
        return new_db_session.query(Session).all()

    def get_session(self, session_id: int):
        new_db_session = db_session.create_session()
        return new_db_session.query(Session).filter(Session.id == session_id)

    def add(self, session: Session):
        new_db_session = db_session.create_session()
        new_db_session.add(session)
        new_db_session.commit()

    def update(self, session_id: int, new_session: Session):
        new_db_session = db_session.create_session()
        session = new_db_session.query(Session).filter(Session.id == session_id)
        session.film_id = new_session.film_id
        session.session_datetime = new_session.session_datetime
        new_db_session.commit()

    def delete(self, session_id: int):
        new_db_session = db_session.create_session()
        new_db_session.delete(new_db_session.query(Session).filter(Session.id == session_id))
        new_db_session.commit()
