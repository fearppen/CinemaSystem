from flask_restful import Resource

from services.films_service import FilmService


class FilmResource(Resource):
    film_service = FilmService()

    def get(self, film_id):
        return self.film_service.get_film(film_id)

    def post(self, film):
        return self.film_service.add(film)

    def put(self, film_id, film):
        return self.film_service.update(film_id, film)

    def delete(self, film_id):
        return self.film_service.delete(film_id)


class FilmListResources(Resource):
    film_service = FilmService()

    def get(self):
        return self.film_service.get_all()
