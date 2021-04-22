from flask_restful import Resource

from services.halls_service import HallService


class HallResource(Resource):
    hall_service = HallService()

    def get(self, hall_id):
        return self.hall_service.get_hall(hall_id)

    def post(self, hall):
        return self.hall_service.add(hall)

    def put(self, hall_id, hall):
        return self.hall_service.update(hall_id, hall)

    def delete(self, hall_id):
        return self.hall_service.delete(hall_id)


class HallListResources(Resource):
    hall_service = HallService()

    def get(self):
        return self.hall_service.get_all()
