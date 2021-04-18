from services.registration_service import RegistrationService


class RegistrationController:
    registration_service = RegistrationService()

    def registration(self, form):
        return self.registration_service.registration(form)
