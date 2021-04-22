from repository.chairs_repository import ChairsRepositorySQLAlchemy


class ChairService:
    chairs_repository = ChairsRepositorySQLAlchemy()

    def get_all(self):
        return {"chairs": [item.to_dict(only=("id", "row", "place", "hall_id"))
                           for item in self.chairs_repository.get_all()]}

    def get_chair(self, chair_id):
        chair = self.chairs_repository.get_chair(chair_id)
        if chair:
            return {"chair": [item.to_dict(only=("id", "row", "place", "hall_id"))
                              for item in [chair]]}
        else:
            return {"error": "Not found"}

    def add(self, chair):
        self.chairs_repository.add(chair)
        return {"success": "ok"}

    def update(self, chair_id, new_chair):
        chair = self.chairs_repository.get_chair(chair_id)
        if chair:
            self.chairs_repository.update(chair_id, new_chair)
            return {"success": "ok"}
        else:
            return {"error": "Not found"}

    def delete(self, chair_id):
        self.chairs_repository.delete(chair_id)
        return {"success": "ok"}
