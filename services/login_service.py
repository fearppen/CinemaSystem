from werkzeug.security import check_password_hash

from forms.authorisation_form import AuthorisationForm
from controllers.users_controller import UsersListResources


def is_this_user_in_bd(all_users: dict, email, password):
    for _, users in all_users.items():
        for i in users:
            flag = False
            for key, value in i.items():
                if key == "email" and value == email:
                    flag = True
                if key == "password" and check_password_hash(value, password) and flag:
                    return ""
                elif flag and key == "password":
                    return "Пароль неверный"
    return "Такого пользователя не существует"


class LoginService:
    def login(self, form: AuthorisationForm):
        email = form.email
        password = form.password
        all_users = UsersListResources().get()
        return is_this_user_in_bd(all_users, email, password)
