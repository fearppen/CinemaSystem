from sqlalchemy import Table, Column, Integer, ForeignKey

from domain.db_session import SqlAlchemyBase

hall_session_table = Table('halls_sessions', SqlAlchemyBase.metadata,
                           Column('hall_id', Integer, ForeignKey('halls.id')),
                           Column('session_id', Integer, ForeignKey('sessions.id')))
