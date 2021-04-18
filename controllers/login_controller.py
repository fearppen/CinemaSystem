from flask_restful import Resource

from forms.authorisation_form import AuthorisationForm
from services.login_service import LoginService


class LoginResource(Resource):
    login_service = LoginService()

    def login(self, form: AuthorisationForm):
        return self.login_service.login(form)
