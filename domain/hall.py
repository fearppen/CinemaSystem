from domain.place import Place
from domain.session import Session


class Hall:
    def __init__(self, places: dict, current_session: Session = None):
        self.current_session = current_session
        self.places = places

    def get_current_session(self):
        return self.current_session

    def get_places(self):
        return self.places

    def set_current_session(self, current_session: Session):
        self.current_session = current_session

    def set_places(self, places: dict):
        self.places = places

    def add_place(self, place: Place):
        self.places[place] = place.get_state()

    def remove_place(self, place: Place):
        self.places.pop(place)
