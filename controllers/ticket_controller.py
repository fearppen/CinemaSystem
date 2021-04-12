from flask import jsonify
from flask_restful import Resource

from services.tickets_service import TicketService


class TicketResource(Resource):
    def get(self, ticket_id):
        return jsonify({"ticket": [item.to_dict for item in TicketService.get_ticket(ticket_id)]})

    def post(self, ticket):
        TicketService.add(ticket)
        return jsonify({'success': 'OK'})

    def put(self, ticket_id, ticket):
        TicketService.update(ticket_id, ticket)
        return jsonify({'success': 'OK'})

    def delete(self, ticket_id):
        TicketService.delete(ticket_id)
        return jsonify({'success': 'OK'})


class TicketsListResources(Resource):
    def get(self):
        return jsonify({"tickets": [item.to_dict for item in TicketService.get_all()]})
