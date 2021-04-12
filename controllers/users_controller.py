from flask import jsonify
from flask_restful import Resource

from services.user_service import UserService


class UserResource(Resource):
    def get(self, user_id: int):
        return jsonify({"user": [item.to_dict for item in UserService.get_user(user_id)]})

    def post(self, user):
        UserService.add(user)
        return jsonify({'success': 'OK'})

    def put(self, user_id, new_user):
        UserService.update(user_id=user_id, new_user=new_user)
        return jsonify({'success': 'OK'})

    def delete(self, user_id):
        UserService.delete(user_id)
        return jsonify({'success': 'OK'})


class UsersListResources(Resource):
    def get(self):
        return jsonify({"users": [item.to_dict for item in UserService.get_all()]})
