from repository.roles_repository import RolesRepositorySQLAlchemy


class RolesService:
    roles_repository = RolesRepositorySQLAlchemy()

    def get_all(self):
        return self.roles_repository.get_all()

    def get_role(self, role_id):
        return self.roles_repository.get_role(role_id)
