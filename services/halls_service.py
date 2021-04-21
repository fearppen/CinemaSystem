from repository.halls_repository import HallsRepositorySQLAlchemy


class HallService:
    halls_repository = HallsRepositorySQLAlchemy()

    def get_all(self):
        return self.halls_repository.get_all()

    def get_hall(self, hall_id):
        return [self.halls_repository.get_hall(hall_id)]

    def add(self, hall):
        return self.halls_repository.add(hall)

    def update(self, hall_id, hall):
        return self.halls_repository.update(hall_id, hall)

    def delete(self, hall_id):
        return self.halls_repository.delete(hall_id)
