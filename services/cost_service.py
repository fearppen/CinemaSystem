from repository.costs_repository import CostsRepositorySQLAlchemy


class CostService:
    cost_repository = CostsRepositorySQLAlchemy()

    def get_all(self):
        return self.cost_repository.get_all()

    def get_cost(self, cost_id):
        return self.cost_repository.get_cost(cost_id)

    def add(self, cost):
        return self.cost_repository.add(cost)

    def update(self, cost_id, cost):
        return self.cost_repository.update(cost_id, cost)

    def delete(self, cost_id):
        return self.cost_repository.delete(cost_id)
