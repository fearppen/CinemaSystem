class Place:
    def __init__(self, row: int, place: int):
        self.row = row
        self.place = place
        self.state = True

    def get_row(self):
        return self.row

    def get_place(self):
        return self.place

    def get_state(self):
        return self.state

    def set_row(self, row: int):
        self.row = row

    def set_place(self, place: int):
        self.place = place

    def set_state(self, value: bool):
        self.state = value
