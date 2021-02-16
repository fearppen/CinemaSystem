from domain.cinema import Cinema
from domain.session import Session
from domain.ticket import Ticket


class Record:
    def __init__(self, cinema: Cinema, session: Session, ticket: Ticket, date: str):
        self.cinema = cinema
        self.session = session
        self.ticket = ticket
        self.date = date

    def get__cinema(self):
        return self.cinema

    def get_session(self):
        return self.session

    def get_ticket(self):
        return self.ticket

    def get_date(self):
        return self.date

    def set_cinema(self, cinema: Cinema):
        self.cinema = cinema

    def set_session(self, session: Session):
        self.session = session

    def set_ticket(self, ticket: Ticket):
        self.ticket = ticket

    def set_date(self, date: str):
        self.date = date
