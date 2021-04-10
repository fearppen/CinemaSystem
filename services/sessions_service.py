from repository.sessions_repository import SessionsRepositorySQLAlchemy


class SessionService:
    def get_all(self):
        return SessionsRepositorySQLAlchemy.get_all()

    def get_session(self, session_id):
        return SessionsRepositorySQLAlchemy.get_session(session_id)

    def add(self, session):
        return SessionsRepositorySQLAlchemy.add(session)

    def update(self, session_id, session):
        return SessionsRepositorySQLAlchemy.update(session_id, session)

    def delete(self, session_id):
        return SessionsRepositorySQLAlchemy.delete(session_id)
