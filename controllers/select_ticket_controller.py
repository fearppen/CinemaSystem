from flask_restful import Resource
from services.select_ticket_service import SelectTicketService


class SelectTicketResource(Resource):
    select_ticket_service = SelectTicketService()

    def get(self, hall_id, session_id):
        return self.select_ticket_service.select_ticket(hall_id, session_id)
