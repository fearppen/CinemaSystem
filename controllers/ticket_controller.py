from flask_restful import Resource

from services.tickets_service import TicketService


class TicketResource(Resource):
    ticket_service = TicketService()

    def get(self, ticket_id):
        return {"ticket": [item.to_dict(only=("id", "number", "cost", "chair_id", "session_id"))
                           for item in self.ticket_service.get_ticket(ticket_id)]}

    def post(self, ticket):
        self.ticket_service.add(ticket)
        return {'success': 'OK'}

    def put(self, ticket_id, ticket):
        self.ticket_service.update(ticket_id, ticket)
        return {'success': 'OK'}

    def delete(self, ticket_id):
        self.ticket_service.delete(ticket_id)
        return {'success': 'OK'}


class TicketsListResources(Resource):
    ticket_service = TicketService()

    def get(self):
        return {"tickets": [item.to_dict(only=("id", "number", "cost", "chair_id", "session_id"))
                            for item in self.ticket_service.get_all()]}
