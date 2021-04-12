from flask import jsonify
from flask_restful import Resource

from services.genre_service import GenreService


class GenreResources(Resource):
    def get(self):
        return jsonify(
            {"genres": [item.to_dict for item in GenreService.all_genres()]}
        )
