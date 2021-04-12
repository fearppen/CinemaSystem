from flask import jsonify
from flask_restful import Resource

from services.roles_service import RolesService


class RoleResource(Resource):
    def get(self, role_id):
        return jsonify({"role": [item.to_dict for item in RolesService.get_role(role_id)]})


class RoleListResources(Resource):
    def get(self):
        return jsonify({"roles": [item.to_dict for item in RolesService.get_all()]})
