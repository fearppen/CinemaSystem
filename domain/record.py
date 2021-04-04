from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from domain.db_session import SqlAlchemyBase


class Record(SqlAlchemyBase):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    purchase_date = Column(DateTime, nullable=False)
    record_type = Column(Integer, nullable=False)

    ticket_id = Column("ticket_id", Integer, ForeignKey("tickets.id"), nullable=False)
    ticket = relationship("Ticket", back_populates='record')

    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates='record')
