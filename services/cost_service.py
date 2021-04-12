from repository.costs_repository import CostsRepositorySQLAlchemy


class CostService:
    def get_all(self):
        return CostsRepositorySQLAlchemy.get_all()

    def get_cost(self, cost_id):
        return CostsRepositorySQLAlchemy.get_cost(cost_id)

    def add(self, cost):
        return CostsRepositorySQLAlchemy.add(cost)

    def update(self, cost_id, cost):
        return CostsRepositorySQLAlchemy.update(cost_id, cost)

    def delete(self, cost_id):
        return CostsRepositorySQLAlchemy.delete(cost_id)
