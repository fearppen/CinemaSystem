from flask_restful import Resource

from services.registration_service import RegistrationService


<<<<<<< HEAD
class RegistrationResource:
=======
class RegistrationResource(Resource):
>>>>>>> 48914a16aa111089133fcb81f95436ced99cc83b
    registration_service = RegistrationService()

    def registration(self, form):
        return self.registration_service.registration(form)
