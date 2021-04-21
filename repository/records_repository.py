from abc import ABC, abstractmethod

from domain import db_session
from domain.record import Record


class IRecordsRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_record(self, record_id: int):
        pass

    @abstractmethod
    def add(self, record: Record):
        pass

    @abstractmethod
    def update(self, record_id: int, new_record: Record):
        pass

    @abstractmethod
    def delete(self, record_id: int):
        pass


class RecordsRepositorySQLAlchemy(IRecordsRepository):
    def get_all(self):
        new_db_session = db_session.create_session()
        return new_db_session.query(Record).all()

    def get_record(self, record_id: int):
        new_db_session = db_session.create_session()
        return new_db_session.query(Record).filter(Record.id == record_id).first()

    def add(self, record: Record):
        new_db_session = db_session.create_session()
        new_db_session.add(record)
        new_db_session.commit()

    def update(self, record_id: int, new_record: Record):
        new_db_session = db_session.create_session()
        record = new_db_session.query(Record).filter(Record.id == record_id).first()
        record.purchase_date = new_record.purchase_date
        record.record_type_id = new_record.record_type_id
        record.ticket_id = new_record.ticket_id
        record.user_id = new_record.user_id
        new_db_session.commit()

    def delete(self, record_id: int):
        new_db_session = db_session.create_session()
        new_db_session.delete(new_db_session.query(Record).filter(Record.id == record_id))
        new_db_session.commit()
