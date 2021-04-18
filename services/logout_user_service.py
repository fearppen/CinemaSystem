from flask_login import logout_user


class LogoutUserService:
    def logout_user(self):
        return logout_user()
