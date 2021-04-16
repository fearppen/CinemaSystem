from flask_restful import Resource

from services.chairs_service import ChairService


class ChairResource(Resource):
    chair_service = ChairService()

    def get(self, chair_id):
        return {"chair": [item.to_dict(only=("row", "place", "hall_id"))
                          for item in self.chair_service.get_chair(chair_id)]}

    def post(self, chair):
        self.chair_service.add(chair)
        return {'success': 'OK'}

    def put(self, chair_id, chair):
        self.chair_service.update(chair_id, chair)
        return {'success': 'OK'}

    def delete(self, chair_id):
        self.chair_service.delete(chair_id)
        return {'success': 'OK'}


class ChairListResources(Resource):
    chair_service = ChairService()

    def get(self):
        return {"chairs": [item.to_dict(only=("row", "place", "hall_id"))
                           for item in self.chair_service.get_all()]}
