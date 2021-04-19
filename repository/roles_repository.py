from abc import ABC, abstractmethod

from domain import db_session
from domain.role import Role


class IRolesRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_role(self, role_id: Role):
        pass


class RolesRepositorySQLAlchemy(IRolesRepository):
    def get_all(self):
        new_db_session = db_session.create_session()
        return new_db_session.query(Role).all()

    def get_role(self, role_id: Role):
        new_db_session = db_session.create_session()
        return new_db_session.query(Role).filter(Role.id == role_id).first()
