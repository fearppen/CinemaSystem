from services.personal_area_service import PersonalAreaService


class PersonalAreaResource:
    personal_area_service = PersonalAreaService()

    def get_user_tickets(self):
        return self.personal_area_service.get_user_tickets()
