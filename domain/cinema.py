from domain.hall import Hall
from domain.session import Session


class Cinema:
    def __init__(self, halls: list, sessions: list):
        self.halls = halls
        self.sessions = sessions

    def get_halls(self):
        return self.halls

    def get_sessions(self):
        return self.sessions

    def set_halls(self, halls: list):
        self.halls = halls

    def set_sessions(self, sessions: list):
        self.sessions = sessions

    def add_hall(self, hall: Hall):
        self.halls.append(hall)

    def remove_hall(self, index: int):
        self.halls.pop(index)

    def add_session(self, session: Session):
        self.sessions.append(session)

    def remove_session(self, index: int):
        self.sessions.pop(index)
