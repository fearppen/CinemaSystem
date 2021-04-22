from repository.users_repository import UsersRepositorySQLAlchemy


class UserService:
    users_repository = UsersRepositorySQLAlchemy()

    def get_all(self):
        return {"users": [item.to_dict(only=("id", "login", "password", "email", "role_id"))
                          for item in self.users_repository.get_all()]}

    def get_user(self, user_id):
        user = self.users_repository.get_user(user_id)
        if user:
            return {"user": [item.to_dict(only=("id", "login", "password", "email", "role_id"))
                             for item in [user]]}
        return {"error": "not found"}

    def add(self, user):
        self.users_repository.add(user)
        return {"success": "ok"}

    def update(self, user_id, new_user):
        if self.users_repository.get_user(user_id):
            self.users_repository.update(user_id, new_user)
            return {"success": "ok"}
        return {"error": "not found"}

    def delete(self, user_id):
        if self.users_repository.get_user(user_id):
            self.users_repository.delete(user_id)
            return {"success": "ok"}
        return {"error": "not found"}
