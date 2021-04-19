from flask_restful import Resource

from services.cinemas_service import CinemasService


class CinemasResource(Resource):
    cinemas_service = CinemasService()

    def get(self, cinema_id):
        return {"cinema": [item.to_dict(only=("id", "title"))
                           for item in self.cinemas_service.get_cinema(cinema_id)]}

    def post(self, cinema):
        self.cinemas_service.add(cinema)
        return {'success': 'OK'}

    def put(self, cinema_id, cinema):
        self.cinemas_service.update(cinema_id, cinema)
        return {'success': 'OK'}

    def delete(self, cinema_id):
        self.cinemas_service.delete(cinema_id)
        return {'success': 'OK'}


class CinemasListResources(Resource):
    cinemas_service = CinemasService()

    def get(self):
        return {"cinemas": [item.to_dict(only=("id", "title")) for item in self.cinemas_service.get_all()]}
