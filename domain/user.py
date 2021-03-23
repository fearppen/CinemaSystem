from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase
from domain.record_user import record_user_table


class User(SqlAlchemyBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)

    records = relationship("Record", secondary=record_user_table, back_populates='user')

    role_id = Column("role_id", Integer, nullable=False)
    role = relationship("Role", back_populates="user")
