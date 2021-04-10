from repository.chairs_repository import ChairsRepositorySQLAlchemy


class ChairService:
    def get_all(self):
        return ChairsRepositorySQLAlchemy.get_all()

    def get_chair(self, chair_id):
        return ChairsRepositorySQLAlchemy.get_chair(chair_id)

    def add(self, chair):
        return ChairsRepositorySQLAlchemy.add(chair)

    def update(self, chair_id, chair):
        return ChairsRepositorySQLAlchemy.update(chair_id, chair)

    def delete(self, chair_id):
        return ChairsRepositorySQLAlchemy.delete(chair_id)
