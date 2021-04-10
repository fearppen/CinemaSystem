from flask import jsonify
from flask_restful import Resource

from services.cinemas_service import CinemasService


class CinemasResource(Resource):
    def get(self, cinema_id):
        return jsonify({"cinema": [item.to_dict for item in CinemasService.get_cinema(cinema_id)]})

    def post(self, cinema):
        CinemasService.add(cinema)
        return jsonify({'success': 'OK'})

    def put(self, cinema_id, cinema):
        CinemasService.update(cinema_id, cinema)
        return jsonify({'success': 'OK'})

    def delete(self, cinema_id):
        CinemasService.delete(cinema_id)
        return jsonify({'success': 'OK'})


class CinemasListResources(Resource):
    def get(self):
        return jsonify({"cinemas": [item.to_dict for item in CinemasService.get_all()]})
