from flask_restful import Resource

from services.genre_service import GenreService


class GenreResources(Resource):
    genre_service = GenreService()

    def get(self, genre_id):
        return {"genres": [item.to_dict(only=("title", "id"))
                           for item in self.genre_service.get_genre(genre_id)]}


class GenreListResources(Resource):
    genre_service = GenreService()

    def get(self):
        return {"genres": [item.to_dict(only=("title", "id")) for item in self.genre_service.all_genres()]}
