from abc import ABC, abstractmethod
from repository.genres_repository import GenresRepositorySQLAlchemy


class IGenreService(ABC):
    @abstractmethod
    def all_genres(self):
        pass


class GenreService(IGenreService):
    def all_genres(self):
        return GenresRepositorySQLAlchemy.get_all()
