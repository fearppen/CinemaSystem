from flask_restful import Resource

from services.registration_service import RegistrationService


class RegistrationResource(Resource):
    registration_service = RegistrationService()

    def post(self, form):
        return self.registration_service.registration(form)
