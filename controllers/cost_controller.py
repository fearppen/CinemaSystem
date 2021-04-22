from flask_restful import Resource

from services.cost_service import CostService


class CostResource(Resource):
    cost_service = CostService()

    def get(self, cost_id):
        return self.cost_service.get_cost(cost_id)

    def post(self, cost):
        return self.cost_service.add(cost)

    def put(self, cost_id, cost):
        return self.cost_service.update(cost_id, cost)

    def delete(self, cost_id):
        return self.cost_service.delete(cost_id)


class CostListResources(Resource):
    cost_service = CostService()

    def get(self):
        return self.cost_service.get_all()
