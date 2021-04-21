from repository.chairs_repository import ChairsRepositorySQLAlchemy


class ChairService:
    chairs_repository = ChairsRepositorySQLAlchemy()

    def get_all(self):
        return self.chairs_repository.get_all()

    def get_chair(self, chair_id):
        return [self.chairs_repository.get_chair(chair_id)]

    def add(self, chair):
        return self.chairs_repository.add(chair)

    def update(self, chair_id, chair):
        return self.chairs_repository.update(chair_id, chair)

    def delete(self, chair_id):
        return self.chairs_repository.delete(chair_id)
