from sqlalchemy import Column, Integer, Date, ForeignKey, String
from sqlalchemy.orm import relationship

from data.db_session import SqlAlchemyBase


class Film(SqlAlchemyBase):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
    duration = Column(String, nullable=False)
    director = Column(String, nullable=False)

    genre_id = Column('genre_id', Integer, ForeignKey('genres.id'), nullable=False)
    genre = relationship('Genre', back_populates='film')

    session = relationship("Session")
