from domain.ticket import Ticket


class Session:
    def __init__(self, tickets: dict, film: str, date: str):
        self.tickets = tickets
        self.film = film
        self.date = date

    def get_tickets(self):
        return self.tickets

    def get_film(self):
        return self.film

    def get_date(self):
        return self.date

    def set_tickets(self, tickets: dict):
        self.tickets = tickets

    def set_film(self, film: str):
        self.film = film

    def set_date(self, date: str):
        self.date = date

    def add_ticket(self, ticket: Ticket):
        self.tickets[ticket] = ticket.get_state()

    def remove_ticket(self, ticket: Ticket):
        self.tickets.pop(ticket)
