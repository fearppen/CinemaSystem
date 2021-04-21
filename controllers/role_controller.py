from flask_restful import Resource

from services.roles_service import RolesService


class RoleResource(Resource):
    roles_service = RolesService()

    def get(self, role_id):
        return {"role": [item.to_dict(only=("id", "title"))
                         for item in self.roles_service.get_role(role_id)]}


class RoleListResources(Resource):
    roles_service = RolesService()

    def get(self):
        return {"roles": [item.to_dict(only=("id", "title"))
                          for item in self.roles_service.get_all()]}
