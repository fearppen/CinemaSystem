from flask_restful import Resource
from services.select_film_by_genre_and_cinema_service import SelectFilmService


class SelectFilmResource(Resource):
    select_film_service = SelectFilmService()

    def get(self, cinema_id, genre_id):
        return {"films": [item.to_dict(
            only=("id", "title", "release_date", "duration", "director", "genre_id"))
            for item in self.select_film_service.select_film(cinema_id, genre_id)]}
