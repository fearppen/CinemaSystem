from repository.users_repository import UsersRepositorySQLAlchemy


class UserService:
    users_repository = UsersRepositorySQLAlchemy()

    def get_all(self):
        return self.users_repository.get_all()

    def get_user(self, user_id: int):
        return self.users_repository.get_user(user_id)

    def add(self, user):
        return self.users_repository.add(user)

    def update(self, user_id, new_user):
        return self.users_repository.update(user_id, new_user)

    def delete(self, user_id):
        return self.users_repository.delete(user_id)
