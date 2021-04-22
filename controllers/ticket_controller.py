from flask_restful import Resource

from services.tickets_service import TicketService


class TicketResource(Resource):
    ticket_service = TicketService()

    def get(self, ticket_id):
        return self.ticket_service.get_ticket(ticket_id)

    def post(self, ticket):
        return self.ticket_service.add(ticket)

    def put(self, ticket_id, ticket):
        return self.ticket_service.update(ticket_id, ticket)

    def delete(self, ticket_id):
        return self.ticket_service.delete(ticket_id)


class TicketsListResources(Resource):
    ticket_service = TicketService()

    def get(self):
        return self.ticket_service.get_all()
