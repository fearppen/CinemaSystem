from flask_restful import Resource

from services.roles_service import RolesService


class RoleResource(Resource):
    roles_service = RolesService()

    def get(self, role_id):
        return self.roles_service.get_role(role_id)


class RoleListResources(Resource):
    roles_service = RolesService()

    def get(self):
        return self.roles_service.get_all()
