from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase


class Cost(SqlAlchemyBase):
    __tablename__ = "costs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cost = Column(Float, nullable=False)

    session_id = Column('session_id', Integer, ForeignKey('sessions.id'), nullable=False)
    session = relationship("Session", back_populates='cost')
