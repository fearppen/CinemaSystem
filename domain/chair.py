from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase
from domain.hall_chair import hall_chair_table


class Chair(SqlAlchemyBase):
    __tablename__ = "chairs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    row = Column(Integer, nullable=False)
    place = Column(Integer, nullable=False)

    hall = relationship("Hall", secondary=hall_chair_table, back_populates='chairs')

    ticket = relationship("Ticket")
