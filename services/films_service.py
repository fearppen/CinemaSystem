from repository.films_repository import FilmsRepositorySQLAlchemy


class FilmService:
    films_repository = FilmsRepositorySQLAlchemy()

    def get_all(self):
        return self.films_repository.get_all()

    def get_film(self, film_id):
        return [self.films_repository.get_film(film_id)]

    def add(self, film):
        return self.films_repository.add(film)

    def update(self, film_id, film):
        return self.films_repository.update(film_id, film)

    def delete(self, film_id):
        return self.films_repository.delete(film_id)
