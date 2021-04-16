from flask_restful import Resource

from services.sessions_service import SessionService


class SessionResource(Resource):
    session_service = SessionService()

    def get(self, session_id):
        return {"session": [item.to_dict(only=("session_datetime", "film_id"))
                            for item in self.session_service.get_session(session_id)]}

    def post(self, session):
        self.session_service.add(session)
        return {'success': 'OK'}

    def put(self, session_id, session):
        self.session_service.update(session_id, session)
        return {'success': 'OK'}

    def delete(self, session_id):
        self.session_service.delete(session_id)
        return {'success': 'OK'}


class SessionListResources(Resource):
    session_service = SessionService()

    def get(self):
        return {"sessions": [item.to_dict(only=("session_datetime", "film_id"))
                             for item in self.session_service.get_all()]}
