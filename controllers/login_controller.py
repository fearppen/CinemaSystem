from forms.authorisation_form import AuthorisationForm
from services.login_service import LoginService


class LoginResource:
    login_service = LoginService()

    def post(self, form: AuthorisationForm):
        return self.login_service.login(form)