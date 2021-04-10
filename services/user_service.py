from repository.users_repository import UsersRepositorySQLAlchemy


class UserService:
    def get_all(self):
        return UsersRepositorySQLAlchemy.get_all()

    def get_user(self, user_id):
        return UsersRepositorySQLAlchemy.get_user(user_id)

    def add(self, user):
        return UsersRepositorySQLAlchemy.add(user)

    def update(self, user_id, new_user):
        return UsersRepositorySQLAlchemy.update(user_id, new_user)

    def delete(self, user_id):
        return UsersRepositorySQLAlchemy.delete(user_id)
