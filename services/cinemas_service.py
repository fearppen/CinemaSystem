from repository.cinemas_repository import CinemasRepositorySQLAlchemy


class CinemasService:
    def get_all(self):
        return CinemasRepositorySQLAlchemy.get_all()

    def get_cinema(self, cinema_id):
        return CinemasRepositorySQLAlchemy.get_cinema(cinema_id)

    def add(self, cinema):
        return CinemasRepositorySQLAlchemy.add(cinema)

    def update(self, cinema_id, cinema):
        return CinemasRepositorySQLAlchemy.update(cinema_id, cinema)

    def delete(self, cinema_id):
        return CinemasRepositorySQLAlchemy.delete(cinema_id)
