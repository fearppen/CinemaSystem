from repository.genres_repository import GenresRepositorySQLAlchemy


class GenreService:
    genres_repository = GenresRepositorySQLAlchemy()

    def all_genres(self):
        return {"genres": [item.to_dict(only=("title", "id"))
                           for item in self.genres_repository.get_all()]}

    def get_genre(self, genre_id):
        genre = self.genres_repository.get_genre(genre_id)
        if genre:
            return {"genres": [item.to_dict(only=("title", "id"))
                               for item in [genre]]}
