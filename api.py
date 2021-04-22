from flask import jsonify, Blueprint, request
from domain.chair import Chair

from controllers.chair_controller import ChairResource, ChairListResources
from controllers.cinemas_controller import CinemasResource, CinemasListResources
from controllers.cost_controller import CostResource, CostListResources
from controllers.film_controller import FilmListResources, FilmResource
from controllers.genre_controller import GenreResources, GenreListResources

from domain.cinema import Cinema
from domain.cost import Cost
from domain.film import Film
from domain.genre import Genre

blueprint = Blueprint("cinema_api", __name__)
chair_resource = ChairResource()
chair_list_resource = ChairListResources()
cinema_resource = CinemasResource()
cinema_list_resource = CinemasListResources()
cost_resource = CostResource()
cost_list_resource = CostListResources()
film_resource = FilmResource()
film_list_resource = FilmListResources()
genre_resource = GenreResources()
genre_list_resource = GenreListResources()


def check_request_chair(req):
    if not req:
        return jsonify({"error": "Empty request"})
    elif not all(key in req for key in
                 ["row", "place", "hall_id"]):
        return jsonify({"error": "Bad request"})
    else:
        chair = Chair()
        chair.row = req["row"]
        chair.place = req["place"]
        chair.hall_id = req["hall_id"]
        return chair


def check_request_cinema(req):
    if not req:
        return jsonify({"error": "Empty request"})
    elif not all(key in req for key in
                 ["title"]):
        return jsonify({"error": "Bad request"})
    else:
        cinema = Cinema()
        cinema.title = req["title"]
        return cinema


def check_request_cost(req):
    if not req:
        return jsonify({"error": "Empty request"})
    elif not all(key in req for key in
                 ["title"]):
        return jsonify({"error": "Bad request"})
    else:
        cost = Cost()
        cost.cost = req["cost"]
        cost.session_id = req["session_id"]
        return cost


def check_request_film(req):
    if not req:
        return jsonify({"error": "Empty request"})
    elif not all(key in req for key in
                 ["title", "release_date", "duration", "director", "genre_id"]):
        return jsonify({"error": "Bad request"})
    else:
        film = Film()
        film.title = req["title"]
        film.release_date = req["release_date"]
        film.duration = req["duration"]
        film.director = req["director"]
        film.genre_id = req["genre_id"]
        return film


def check_request_genre(req):
    if not req:
        return jsonify({"error": "Empty request"})
    elif not all(key in req for key in
                 ["title"]):
        return jsonify({"error": "Bad request"})
    else:
        genre = Genre()
        genre.title = req["title"]
        return genre


@blueprint.route("/api/chair")
def get_all_chairs():
    return jsonify(chair_list_resource.get())


@blueprint.route("/api/chair/<int:chair_id>")
def get_one_chair(chair_id):
    return jsonify(chair_resource.get(chair_id))


@blueprint.route("api/chair", methods=["POST"])
def create_chair():
    return jsonify(chair_resource.post(check_request_chair(request.json)))


@blueprint.route("api/chair/<int:chair_id>", methods=["PUT"])
def edit_chair(chair_id):
    return jsonify(chair_resource.put(chair_id, check_request_chair(request.json)))


@blueprint.route("api/chair/<int:chair_id>", methods=["DELETE"])
def delete_chair(chair_id):
    return jsonify(chair_resource.delete(chair_id))


@blueprint.route("/api/cinema")
def get_all_cinemas():
    return jsonify(cinema_list_resource.get())


@blueprint.route("/api/cinema/<int:cinema_id>")
def get_one_cinema(cinema_id):
    return jsonify(cinema_resource.get(cinema_id))


@blueprint.route("api/cinema", methods=["POST"])
def create_cinema():
    return jsonify(cinema_resource.post(check_request_cinema(request.json)))


@blueprint.route("api/cinema/<int:cinema_id>", methods=["PUT"])
def edit_cinema(cinema_id):
    return jsonify(cinema_resource.put(cinema_id, check_request_cinema(request.json)))


@blueprint.route("api/cinema/<int:cinema_id>", methods=["DELETE"])
def delete_cinema(cinema_id):
    return jsonify(cinema_resource.delete(cinema_id))


@blueprint.route("/api/cost")
def get_all_cost():
    return jsonify(cost_list_resource.get())


@blueprint.route("/api/cost/<int:cost_id>")
def get_one_cost(cost_id):
    return jsonify(cost_resource.get(cost_id))


@blueprint.route("api/cost", methods=["POST"])
def create_cost():
    return jsonify(cost_resource.post(check_request_cost(request.json)))


@blueprint.route("api/cost/<int:cost_id", methods=["PUT"])
def edit_cost(cost_id):
    return jsonify(cost_resource.put(cost_id, check_request_cost(request.json)))


@blueprint.route("api/cost/<int:cost_id>", methods=["DELETE"])
def delete_cost(cost_id):
    return jsonify(cost_resource.delete(cost_id))


@blueprint.route("/api/film")
def get_all_film():
    return jsonify(film_list_resource.get())


@blueprint.route("/api/film/<int:film_id>")
def get_one_film(film_id):
    return jsonify(film_resource.get(film_id))


@blueprint.route("api/film", methods=["POST"])
def create_film():
    return jsonify(film_resource.post(check_request_film(request.json)))


@blueprint.route("api/film/<int:film_id", methods=["PUT"])
def edit_film(film_id):
    return jsonify(film_resource.put(film_id, check_request_film(request.json)))


@blueprint.route("api/film/<int:film_id>", methods=["DELETE"])
def delete_film(film_id):
    return jsonify(film_resource.delete(film_id))


@blueprint.route("/api/genre")
def get_all_genre():
    return jsonify(genre_list_resource.get())


@blueprint.route("/api/genre/<int:genre_id>")
def get_one_film(genre_id):
    return jsonify(genre_id)


@blueprint.route("api/genre", methods=["POST"])
def create_genre():
    return jsonify(genre_resource.post(check_request_genre(request.json)))


@blueprint.route("api/genre/<int:genre_id", methods=["PUT"])
def edit_genre(genre_id):
    return jsonify(genre_resource.put(genre_id, check_request_genre(request.json)))


@blueprint.route("api/genre/<int:genre_id>", methods=["DELETE"])
def delete_genre(genre_id):
    return jsonify(genre_resource.delete(genre_id))
