from flask_restful import Resource

from services.cinemas_service import CinemasService


class CinemasResource(Resource):
    cinemas_service = CinemasService()

    def get(self, cinema_id):
        return self.cinemas_service.get_cinema(cinema_id)

    def post(self, cinema):
        return self.cinemas_service.add(cinema)

    def put(self, cinema_id, cinema):
        return self.cinemas_service.update(cinema_id, cinema)

    def delete(self, cinema_id):
        return self.cinemas_service.delete(cinema_id)


class CinemasListResources(Resource):
    cinemas_service = CinemasService()

    def get(self):
        return self.cinemas_service.get_all()
