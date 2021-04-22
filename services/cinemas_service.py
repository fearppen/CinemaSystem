from repository.cinemas_repository import CinemasRepositorySQLAlchemy


class CinemasService:
    cinemas_repository = CinemasRepositorySQLAlchemy()

    def get_all(self):
        return {"cinemas": [item.to_dict(only=("id", "title"))
                            for item in self.cinemas_repository.get_all()]}

    def get_cinema(self, cinema_id):
        cinema = self.cinemas_repository.get_cinema(cinema_id)
        if cinema:
            return {"cinema": [item.to_dict(only=("id", "title"))
                               for item in [cinema]]}
        return {"error": "not found"}

    def add(self, cinema):
        self.cinemas_repository.add(cinema)
        return {"success": "ok"}

    def update(self, cinema_id, cinema):
        if self.cinemas_repository.get_cinema(cinema_id):
            self.cinemas_repository.update(cinema_id, cinema)
            return {"success": "ok"}
        return {"error": "not found"}

    def delete(self, cinema_id):
        if self.cinemas_repository.get_cinema(cinema_id):
            self.cinemas_repository.delete(cinema_id)
            return {"success": "ok"}
        return {"error": "not found"}