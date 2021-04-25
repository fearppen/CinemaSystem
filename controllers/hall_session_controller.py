from flask_restful import Resource

from domain.hall import Hall
from domain.session import Session
from services.hall_session_service import HallSessionService


class HallSessionResource(Resource):
    hall_session_service = HallSessionService()

    def get(self, hall_id):
        return self.hall_session_service.get_hall_sessions(hall_id)

    def post(self, hall: Hall, session: Session):
        return self.hall_session_service.add(hall, session)

    def put(self, hall: Hall, session: Session, new_session: Session):
        return self.hall_session_service.update(hall, session, new_session)

    def delete(self, hall: Hall, session: Session):
        return self.hall_session_service.delete(hall, session)


class HallSessionListResources(Resource):
    hall_session_service = HallSessionService()

    def get(self):
        return self.hall_session_service.get_all()
