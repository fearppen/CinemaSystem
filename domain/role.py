from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase


class Role(SqlAlchemyBase):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)

    user = relationship("User")
