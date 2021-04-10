from flask import jsonify
from flask_restful import Resource

from services.films_service import FilmService


class FilmResource(Resource):
    def get(self, film_id):
        return jsonify({"film": [item.to_dict for item in FilmService.get_film(film_id)]})

    def post(self, film):
        FilmService.add(film)
        return jsonify({'success': 'OK'})

    def put(self, film_id, film):
        FilmService.update(film_id, film)
        return jsonify({'success': 'OK'})

    def delete(self, film_id):
        FilmService.delete(film_id)
        return jsonify({'success': 'OK'})


class FilmListResources(Resource):
    def get(self):
        return jsonify({"films": [item.to_dict for item in FilmService.get_all()]})
