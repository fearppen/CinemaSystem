from repository.films_repository import FilmsRepositorySQLAlchemy


class FilmService:
    def get_all(self):
        return FilmsRepositorySQLAlchemy.get_all()

    def get_film(self, film_id):
        return FilmsRepositorySQLAlchemy.get_film(film_id)

    def add(self, film):
        return FilmsRepositorySQLAlchemy.add(film)

    def update(self, film_id, film):
        return FilmsRepositorySQLAlchemy.update(film_id, film)

    def delete(self, film_id):
        return FilmsRepositorySQLAlchemy.delete(film_id)
