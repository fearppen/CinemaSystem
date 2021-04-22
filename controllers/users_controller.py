from flask_restful import Resource
from services.user_service import UserService


class UserResource(Resource):
    user_service = UserService()

    def get(self, user_id):
        return self.user_service.get_user(user_id)

    def post(self, user):
        return self.user_service.add(user)

    def put(self, user_id, new_user):
        return self.user_service.update(user_id=user_id, new_user=new_user)

    def delete(self, user_id):
        return self.user_service.delete(user_id)


class UsersListResources(Resource):
    user_service = UserService()

    def get(self):
        return self.user_service.get_all()
