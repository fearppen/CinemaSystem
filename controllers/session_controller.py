from flask import jsonify
from flask_restful import Resource

from services.sessions_service import SessionService


class SessionResource(Resource):
    def get(self, session_id):
        return jsonify({"session": [item.to_dict for item in
                                    SessionService.get_session(session_id)]})

    def post(self, session):
        SessionService.add(session)
        return jsonify({'success': 'OK'})

    def put(self, session_id, session):
        SessionService.update(session_id, session)
        return jsonify({'success': 'OK'})

    def delete(self, session_id):
        SessionService.delete(session_id)
        return jsonify({'success': 'OK'})


class SessionListResources(Resource):
    def get(self):
        return jsonify({"sessions": [item.to_dict for item in SessionService.get_all()]})
