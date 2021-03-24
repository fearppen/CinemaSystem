from abc import ABC, abstractmethod
from services.genre_service import GenreService
from flask import jsonify


class IGenreResources(ABC):
    @abstractmethod
    def get_genres(self):
        pass


class GenreResources(IGenreResources):
    def get_genres(self):
        return jsonify(
            {"genres": [item.to_dict for item in GenreService.all_genres()]}
        )
