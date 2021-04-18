from flask_login import login_user
from werkzeug.security import check_password_hash

from domain.user import User
from forms.authorisation_form import AuthorisationForm
from controllers.users_controller import UsersListResources


def is_this_user_in_bd(all_users: dict, form: AuthorisationForm, email, password):
    for _, users in all_users.items():
        for i in users:
            flag = False
            for key, value in sorted(i.items(), key=lambda x: x[0]):
                if key == "email" and value == email.data:
                    flag = True
                if flag and key == "password":
                    if check_password_hash(value, password.data):
                        login_user(User(login=i["login"], email=i["email"], password=i["password"], role_id=i["role_id"]), remember=form.remember_me.data)
                        return ""
                    else:
                        return "Пароль неверный"
    return "Такого пользователя не существует"


class LoginService:
    def login(self, form: AuthorisationForm):
        email = form.email
        password = form.password
        all_users = UsersListResources().get()
        return is_this_user_in_bd(all_users, form, email, password)
