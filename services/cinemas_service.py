from repository.cinemas_repository import CinemasRepositorySQLAlchemy


class CinemasService:
    cinemas_service = CinemasRepositorySQLAlchemy()

    def get_all(self):
        return self.cinemas_service.get_all()

    def get_cinema(self, cinema_id):
        return [self.cinemas_service.get_cinema(cinema_id)]

    def add(self, cinema):
        return self.cinemas_service.add(cinema)

    def update(self, cinema_id, cinema):
        return self.cinemas_service.update(cinema_id, cinema)

    def delete(self, cinema_id):
        return self.cinemas_service.delete(cinema_id)
