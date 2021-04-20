from flask_restful import Resource

from services.films_service import FilmService


class FilmResource(Resource):
    film_service = FilmService()

    def get(self, film_id):
        return {"film":
                    [item.to_dict(only=("id", "title", "release_date", "duration", "director", "genre_id"))
                     for item in self.film_service.get_film(film_id)]}

    def post(self, film):
        self.film_service.add(film)
        return {'success': 'OK'}

    def put(self, film_id, film):
        self.film_service.update(film_id, film)
        return {'success': 'OK'}

    def delete(self, film_id):
        self.film_service.delete(film_id)
        return {'success': 'OK'}


class FilmListResources(Resource):
    film_service = FilmService()

    def get(self):
        return {"films":
                    [item.to_dict(only=("id", "title", "release_date", "duration", "director", "genre_id"))
                     for item in self.film_service.get_all()]}
