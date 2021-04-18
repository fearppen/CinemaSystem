from services.logout_user_service import LogoutUserService


class LogoutUser:
    logout_user_service = LogoutUserService()

    def logout(self):
        return self.logout_user_service.logout_user()
