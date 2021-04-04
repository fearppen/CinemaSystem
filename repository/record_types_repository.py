from abc import ABC, abstractmethod

from domain import db_session
from domain.record_type import RecordType


class IRecordTypesRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_record_type(self, record_type_id: RecordType):
        pass


class RecordTypesRepositorySQLAlchemy(IRecordTypesRepository):
    def get_all(self):
        new_db_session = db_session.create_session()
        return new_db_session.query(RecordType).all()

    def get_record_type(self, record_type_id: RecordType):
        new_db_session = db_session.create_session()
        return new_db_session.query(RecordType).filter(RecordType.id == record_type_id)
