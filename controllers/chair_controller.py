from flask import jsonify
from flask_restful import Resource

from services.chairs_service import ChairService


class ChairResource(Resource):
    def get(self, chair_id):
        return jsonify({"chair": [item.to_dict for item in ChairService.get_chair(chair_id)]})

    def post(self, chair):
        ChairService.add(chair)
        return jsonify({'success': 'OK'})

    def put(self, chair_id, chair):
        ChairService.update(chair_id, chair)
        return jsonify({'success': 'OK'})

    def delete(self, chair_id):
        ChairService.delete(chair_id)
        return jsonify({'success': 'OK'})


class ChairListResources(Resource):
    def get(self):
        return jsonify({"chairs": [item.to_dict for item in ChairService.get_all()]})
