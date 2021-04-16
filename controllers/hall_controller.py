from flask_restful import Resource

from services.halls_service import HallService


class HallResource(Resource):
    hall_service = HallService()

    def get(self, hall_id):
        return {"hall": [item.to_dict(only=("title", "cinema_id"))
                         for item in self.hall_service.get_hall(hall_id)]}

    def post(self, hall):
        self.hall_service.add(hall)
        return {'success': 'OK'}

    def put(self, hall_id, hall):
        self.hall_service.update(hall_id, hall)
        return {'success': 'OK'}

    def delete(self, hall_id):
        self.hall_service.delete(hall_id)
        return {'success': 'OK'}


class HallListResources(Resource):
    hall_service = HallService()

    def get(self):
        return {"halls": [item.to_dict(only=("title", "cinema_id"))
                          for item in self.hall_service.get_all()]}
