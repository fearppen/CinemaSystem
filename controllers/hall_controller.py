from flask import jsonify
from flask_restful import Resource

from services.halls_service import HallService


class HallResource(Resource):
    def get(self, hall_id):
        return jsonify({"hall": [item.to_dict for item in HallService.get_hall(hall_id)]})

    def post(self, hall):
        HallService.add(hall)
        return jsonify({'success': 'OK'})

    def put(self, hall_id, hall):
        HallService.update(hall_id, hall)
        return jsonify({'success': 'OK'})

    def delete(self, hall_id):
        HallService.delete(hall_id)
        return jsonify({'success': 'OK'})


class HallListResources(Resource):
    def get(self):
        return jsonify({"halls": [item.to_dict for item in HallService.get_all()]})
