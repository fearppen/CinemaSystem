from flask_restful import Resource

from services.chairs_service import ChairService


class ChairResource(Resource):
    chair_service = ChairService()

    def get(self, chair_id):
        return self.chair_service.get_chair(chair_id)

    def post(self, chair):
        return self.chair_service.add(chair)

    def put(self, chair_id, chair):
        return self.chair_service.update(chair_id, chair)

    def delete(self, chair_id):
        return self.chair_service.delete(chair_id)


class ChairListResources(Resource):
    chair_service = ChairService()

    def get(self):
        return self.chair_service.get_all()
