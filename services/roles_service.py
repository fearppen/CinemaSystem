from repository.roles_repository import RolesRepositorySQLAlchemy


class RolesService:
    roles_repository = RolesRepositorySQLAlchemy()

    def get_all(self):
        return {"roles": [item.to_dict(only=("id", "title"))
                          for item in self.roles_repository.get_all()]}

    def get_role(self, role_id):
        role = self.roles_repository.get_role(role_id)
        if role:
            return {"role": [item.to_dict(only=("id", "title"))
                             for item in [role]]}
        return {"error": "not found"}
