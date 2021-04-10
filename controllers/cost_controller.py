from flask import jsonify
from flask_restful import Resource

from services.cost_service import CostService


class CostResource(Resource):
    def get(self, cost_id):
        return jsonify({"cost": [item.to_dict for item in CostService.get_cost(cost_id)]})

    def post(self, cost):
        CostService.add(cost)
        return jsonify({'success': 'OK'})

    def put(self, cost_id, cost):
        CostService.update(cost_id, cost)
        return jsonify({'success': 'OK'})

    def delete(self, cost_id):
        CostService.delete(cost_id)
        return jsonify({'success': 'OK'})


class CostListResources(Resource):
    def get(self):
        return jsonify({"costs": [item.to_dict for item in CostService.get_all()]})
