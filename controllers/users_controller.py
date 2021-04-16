from flask_restful import Resource
from services.user_service import UserService


class UserResource(Resource):
    user_service = UserService()

    def get(self, user_id: int):
        return {"user": [item.to_dict(only=("login", "password", "email"))
                         for item in self.user_service.get_user(user_id)]}

    def post(self, user):
        self.user_service.add(user)
        return {'success': 'OK'}

    def put(self, user_id, new_user):
        self.user_service.update(user_id=user_id, new_user=new_user)
        return {'success': 'OK'}

    def delete(self, user_id):
        self.user_service.delete(user_id)
        return {'success': 'OK'}


class UsersListResources(Resource):
    user_service = UserService()

    def get(self):
        return {"users": [item.to_dict(only=("login", "password", "email"))
                          for item in self.user_service.get_all()]}
