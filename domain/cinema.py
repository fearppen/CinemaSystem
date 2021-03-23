from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase


class Cinema(SqlAlchemyBase):
    __tablename__ = "cinemas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)

    hall = relationship("Hall")
