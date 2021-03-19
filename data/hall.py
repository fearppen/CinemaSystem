from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from data.db_session import SqlAlchemyBase
from data.hall_chair import hall_chair_table
from data.hall_session import hall_session_table


class Hall(SqlAlchemyBase):
    __tablename__ = "halls"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)

    cinema_id = Column("cinema_id", Integer, ForeignKey('cinemas.id'), nullable=False)
    cinema = relationship("Cinema", back_populates='hall')

    session = relationship("Session", secondary=hall_session_table, back_populates='halls')

    chairs = relationship("Chair", secondary=hall_chair_table, back_populates='hall')
