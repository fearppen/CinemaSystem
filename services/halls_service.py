from repository.halls_repository import HallsRepositorySQLAlchemy


class HallService:
    def get_all(self):
        return HallsRepositorySQLAlchemy.get_all()

    def get_hall(self, hall_id):
        return HallsRepositorySQLAlchemy.get_hall(hall_id)

    def add(self, hall):
        return HallsRepositorySQLAlchemy.add(hall)

    def update(self, hall_id, hall):
        return HallsRepositorySQLAlchemy.update(hall_id, hall)

    def delete(self, hall_id):
        return HallsRepositorySQLAlchemy.delete(hall_id)
