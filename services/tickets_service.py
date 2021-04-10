from repository.tickets_repository import TicketsRepositorySQLAlchemy


class TicketService:
    def get_all(self):
        return TicketsRepositorySQLAlchemy.get_all()

    def get_ticket(self, ticket_id):
        return TicketsRepositorySQLAlchemy.get_ticket(ticket_id)

    def add(self, ticket):
        return TicketsRepositorySQLAlchemy.add(ticket)

    def update(self, ticket_id, ticket):
        return TicketsRepositorySQLAlchemy.update(ticket_id, ticket)

    def delete(self, ticket_id):
        return TicketsRepositorySQLAlchemy.delete(ticket_id)
