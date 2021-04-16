from repository.sessions_repository import SessionsRepositorySQLAlchemy


class SessionService:
    sessions_repository = SessionsRepositorySQLAlchemy()

    def get_all(self):
        return self.sessions_repository.get_all()

    def get_session(self, session_id):
        return self.sessions_repository.get_session(session_id)

    def add(self, session):
        return self.sessions_repository.add(session)

    def update(self, session_id, session):
        return self.sessions_repository.update(session_id, session)

    def delete(self, session_id):
        return self.sessions_repository.delete(session_id)
