from domain.hall import Hall
from domain.session import Session
from repository.halls_sessions_repository import HallsSessionsRepositorySQLAlchemy
from services.halls_service import HallService
from services.sessions_service import SessionService


class HallSessionService:
    halls_sessions_repository = HallsSessionsRepositorySQLAlchemy()
    hall_service = HallService()
    session_service = SessionService()

    def get_all(self):
        halls_sessions = self.halls_sessions_repository.get_all()
        for i in range(len(halls_sessions)):
            halls_sessions[i] = (self.hall_service.get_hall(halls_sessions[i][0])[0],
                                 self.session_service.get_session(halls_sessions[i][1])[0])
        return halls_sessions

    def get_hall_sessions(self, hall_id):
        hall_sessions = self.halls_sessions_repository.get_hall_sessions(hall_id)
        for i in range(len(hall_sessions)):
            hall_sessions[i] = (self.hall_service.get_hall(hall_sessions[i][0])[0],
                                self.session_service.get_session(hall_sessions[i][1])[0])
        return hall_sessions

    def add(self, hall: Hall, session: Session):
        return self.halls_sessions_repository.add(hall, session)

    def update(self, hall: Hall, session: Session, new_session: Session):
        return self.halls_sessions_repository.update(hall, session, new_session)

    def delete(self, hall: Hall, session: Session):
        return self.halls_sessions_repository.delete(hall, session)
