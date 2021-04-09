from abc import ABC, abstractmethod

from domain import db_session
from domain.ticket import Ticket


class ITicketsRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_ticket(self, ticket_id: int):
        pass

    @abstractmethod
    def add(self, ticket: Ticket):
        pass

    @abstractmethod
    def update(self, ticket_id: int, new_ticket: Ticket):
        pass

    @abstractmethod
    def delete(self, ticket_id: int):
        pass


class TicketsRepositorySQLAlchemy(ITicketsRepository):
    def get_all(self):
        new_db_session = db_session.create_session()
        return new_db_session.query(Ticket).all()

    def get_ticket(self, ticket_id: int):
        new_db_session = db_session.create_session()
        return new_db_session.query(Ticket).filter(Ticket.id == ticket_id)

    def add(self, ticket: Ticket):
        new_db_session = db_session.create_session()
        new_db_session.add(ticket)
        new_db_session.commit()

    def update(self, ticket_id: int, new_ticket: Ticket):
        new_db_session = db_session.create_session()
        ticket = new_db_session.query(Ticket).filter(Ticket.id == ticket_id)
        ticket.number = new_ticket.number
        ticket.cost = new_ticket.cost
        ticket.chair_id = new_ticket.chair_id
        ticket.session_id = new_ticket.session_id
        new_db_session.commit()

    def delete(self, ticket_id: int):
        new_db_session = db_session.create_session()
        new_db_session.delete(new_db_session.query(Ticket).filter(Ticket.id == ticket_id))
        new_db_session.commit()
