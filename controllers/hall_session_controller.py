from flask_restful import Resource

from domain.hall import Hall
from domain.session import Session
from services.hall_session_service import HallSessionService


class HallSessionResource(Resource):
    hall_session_service = HallSessionService()

    def get(self, hall_id):
        return {"hall_sessions": [item.to_dict(only=("hall_id", "session_id"))
                                  for item in self.hall_session_service.get_hall_sessions(hall_id)]}

    def post(self, hall: Hall, session: Session):
        self.hall_session_service.add(hall, session)
        return {'success': 'OK'}

    def put(self, hall: Hall, session: Session, new_session: Session):
        self.hall_session_service.update(hall, session, new_session)
        return {'success': 'OK'}

    def delete(self, hall: Hall, session: Session):
        self.hall_session_service.delete(hall, session)
        return {'success': 'OK'}


class HallSessionListResources(Resource):
    hall_session_service = HallSessionService()

    def get(self):
        return {"halls_sessions": [{"hall_id": hall.id, "session_id": session.id}
                                   for hall, session in self.hall_session_service.get_all()]}
