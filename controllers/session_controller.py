from flask_restful import Resource

from services.sessions_service import SessionService


class SessionResource(Resource):
    session_service = SessionService()

    def get(self, session_id):
        return self.session_service.get_session(session_id)

    def post(self, session):
        return self.session_service.add(session)

    def put(self, session_id, session):
        return self.session_service.update(session_id, session)

    def delete(self, session_id):
        return self.session_service.delete(session_id)


class SessionListResources(Resource):
    session_service = SessionService()

    def get(self):
        return self.session_service.get_all()
