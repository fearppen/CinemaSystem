from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase


class RecordType(SqlAlchemyBase):  # модель для работы с таблицей типов записей
    __tablename__ = "record_types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)

    record = relationship("Record")
