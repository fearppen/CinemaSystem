from repository.roles_repository import RolesRepositorySQLAlchemy


class RolesService:
    def get_all(self):
        return RolesRepositorySQLAlchemy.get_all()

    def get_role(self, role_id):
        return RolesRepositorySQLAlchemy.get_role(role_id)
