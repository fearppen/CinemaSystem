from domain.hall import Hall
from domain.place import Place


class Ticket:
    def __init__(self, place: Place, hall: Hall, number: str):
        self.place = place
        self.hall = hall
        self.number = number
        self.state = True

    def get_place(self):
        return self.place

    def get_hall(self):
        return self.hall

    def get_number(self):
        return self.number

    def get_state(self):
        return self.state

    def set_place(self, place: Place):
        self.place = place

    def set_hall(self, hall: Hall):
        self.hall = hall

    def set_number(self, number: str):
        self.number = number

    def set_state(self, value: bool):
        self.state = value
