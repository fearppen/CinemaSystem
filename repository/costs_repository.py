from abc import ABC, abstractmethod

from domain import db_session
from domain.cost import Cost


class ICostsRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_cost(self, cost_id: int):
        pass

    @abstractmethod
    def add(self, cost: Cost):
        pass

    @abstractmethod
    def update(self, cost_id: int, new_cost: Cost):
        pass

    @abstractmethod
    def delete(self, cost_id: int):
        pass


class CostsRepositorySQLAlchemy(ICostsRepository):
    def get_all(self):
        new_db_session = db_session.create_session()
        return new_db_session.query(Cost).all()

    def get_cost(self, cost_id: int):
        new_db_session = db_session.create_session()
        return new_db_session.query(Cost).filter(Cost.id == cost_id).first()

    def add(self, cost: Cost):
        new_db_session = db_session.create_session()
        new_db_session.add(cost)
        new_db_session.commit()

    def update(self, cost_id: int, new_cost: Cost):
        new_db_session = db_session.create_session()
        cost = new_db_session.query(Cost).filter(Cost.id == cost_id).first()
        cost.cost = new_cost.cost
        cost.session_id = new_cost.session_id
        new_db_session.commit()

    def delete(self, cost_id: int):
        new_db_session = db_session.create_session()
        new_db_session.delete(new_db_session.query(Cost).filter(Cost.id == cost_id))
        new_db_session.commit()
