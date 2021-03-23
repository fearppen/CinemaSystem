from sqlalchemy import Table, Column, Integer, ForeignKey

from domain.db_session import SqlAlchemyBase

record_user_table = Table('records_users', SqlAlchemyBase.metadata,
                          Column('record_id', Integer, ForeignKey('records.id')),
                          Column('user_id', Integer, ForeignKey('users.id')))
