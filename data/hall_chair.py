from sqlalchemy import Table, Column, Integer, ForeignKey

from data.db_session import SqlAlchemyBase

hall_chair_table = Table('halls_chairs', SqlAlchemyBase.metadata,
                         Column('hall_id', Integer, ForeignKey('halls.id')),
                         Column('chair_id', Integer, ForeignKey('chairs.id')))
