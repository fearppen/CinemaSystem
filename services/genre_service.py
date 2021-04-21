from repository.genres_repository import GenresRepositorySQLAlchemy


class GenreService:
    genres_repository = GenresRepositorySQLAlchemy()

    def all_genres(self):
        return self.genres_repository.get_all()

    def get_genre(self, genre_id):
        return [self.genres_repository.get_genre(genre_id)]
