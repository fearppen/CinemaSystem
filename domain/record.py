from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase
from domain.record_user import record_user_table


class Record(SqlAlchemyBase):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    purchase_date = Column(DateTime, nullable=False)
    record_type = Column(Integer, nullable=False)

    ticket_id = Column("ticket_id", Integer, ForeignKey("tickets.id"), nullable=False)
    ticket = relationship("Ticket", back_populates='record')

    user = relationship("User", secondary=record_user_table, back_populates='records')
