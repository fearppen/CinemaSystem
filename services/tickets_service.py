from repository.tickets_repository import TicketsRepositorySQLAlchemy


class TicketService:
    tickets_repository = TicketsRepositorySQLAlchemy()

    def get_all(self):
        return self.tickets_repository.get_all()

    def get_ticket(self, ticket_id):
        return [self.tickets_repository.get_ticket(ticket_id)]

    def add(self, ticket):
        return self.tickets_repository.add(ticket)

    def update(self, ticket_id, ticket):
        return self.tickets_repository.update(ticket_id, ticket)

    def delete(self, ticket_id):
        return self.tickets_repository.delete(ticket_id)
