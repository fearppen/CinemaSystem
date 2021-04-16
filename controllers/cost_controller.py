from flask_restful import Resource

from services.cost_service import CostService


class CostResource(Resource):
    cost_service = CostService()

    def get(self, cost_id):
        return {"cost": [item.to_dict(only=("cost", "session_id"))
                         for item in self.cost_service.get_cost(cost_id)]}

    def post(self, cost):
        self.cost_service.add(cost)
        return {'success': 'OK'}

    def put(self, cost_id, cost):
        self.cost_service.update(cost_id, cost)
        return {'success': 'OK'}

    def delete(self, cost_id):
        self.cost_service.delete(cost_id)
        return {'success': 'OK'}


class CostListResources(Resource):
    cost_service = CostService()

    def get(self):
        return {"costs": [item.to_dict(only=("cost", "session_id"))
                          for item in self.cost_service.get_all()]}
