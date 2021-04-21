from controllers.film_controller import FilmListResources
from controllers.genre_controller import GenreResources
from controllers.hall_controller import HallListResources


class SelectFilmService:
    hall_resource = HallListResources()

    def select_film(self, cinema_id, genre_id):
        all_halls = self.hall_resource.get()
        halls = []
        for i in all_halls["halls"]:
            for j in i:
                if j["cinema_id"] == cinema_id:
                    halls.append(j["id"])

