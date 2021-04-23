from flask import jsonify, Blueprint, request
from werkzeug.security import generate_password_hash

from domain.chair import Chair

from controllers.chair_controller import ChairResource, ChairListResources
from controllers.cinemas_controller import CinemasResource, CinemasListResources
from controllers.cost_controller import CostResource, CostListResources
from controllers.film_controller import FilmListResources, FilmResource
from controllers.genre_controller import GenreResources, GenreListResources
from controllers.hall_controller import HallResource, HallListResources
from controllers.record_controller import RecordListResources, RecordResource
from controllers.record_types_controller import RecordTypesListResources, RecordTypesResource
from controllers.role_controller import RoleListResources, RoleResource
from controllers.session_controller import SessionListResources, SessionResource
from controllers.ticket_controller import TicketResource, TicketsListResources
from controllers.users_controller import UserResource, UsersListResources

from domain.cinema import Cinema
from domain.cost import Cost
from domain.film import Film
from domain.genre import Genre
from domain.hall import Hall
from domain.record import Record
from domain.session import Session
from domain.ticket import Ticket
from domain.user import User

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
hall_resource = HallResource()
hall_list_resource = HallListResources()
record_resource = RecordResource()
record_list_resource = RecordListResources()
record_type_resource = RecordTypesResource()
record_type_list_resource = RecordTypesListResources()
role_resource = RoleResource()
role_list_resource = RoleListResources()
session_resource = SessionResource()
session_list_resource = SessionListResources()
ticket_resource = TicketResource()
ticket_list_resource = TicketsListResources()
user_resource = UserResource()
user_list_resource = UsersListResources()


def check_request_chair(req):
    if not req.args:
        return jsonify({"error": "Empty request"})
    elif not all(key in req.args for key in
                 ["row", "place", "hall_id"]):
        return jsonify({"error": "Bad request"})
    else:
        chair = Chair()
        chair.row = req.args["row"]
        chair.place = req.args["place"]
        chair.hall_id = req.args["hall_id"]
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


def check_request_hall(req):
    if not req:
        return jsonify({"error": "Empty request"})
    elif not all(key in req for key in
                 ["title", "cinema_id"]):
        return jsonify({"error": "Bad request"})
    else:
        hall = Hall()
        hall.title = req["title"]
        hall.cinema_id = req["cinema_id"]
        return hall


def check_request_record(req):
    if not req:
        return jsonify({"error": "Empty request"})
    elif not all(key in req for key in
                 ["purchase_date", "record_type_id", "ticket_id", "user_id"]):
        return jsonify({"error": "Bad request"})
    else:
        record = Record()
        record.purchase_date = req["purchase_date"]
        record.record_type_id = req["record_type_id"]
        record.ticket_id = req["ticket_id"]
        record.user_id = req["user_id"]
        return record


def check_request_session(req):
    if not req:
        return jsonify({"error": "Empty request"})
    elif not all(key in req for key in
                 ["session_datetime", "film_id"]):
        return jsonify({"error": "Bad request"})
    else:
        session = Session()
        session.session_datetime = req["session_datetime"]
        session.film_id = req["film_id"]
        return session


def check_request_ticket(req):
    if not req:
        return jsonify({"error": "Empty request"})
    elif not all(key in req for key in
                 ["number", "cost", "chair_id", "session_id"]):
        return jsonify({"error": "Bad request"})
    else:
        ticket = Ticket()
        ticket.number = req["number"]
        ticket.cost = req["cost"]
        ticket.chair_id = req["chair_id"]
        ticket.session_id = req["session_id"]
        return ticket


def check_request_user(req):
    if not req:
        return jsonify({"error": "Empty request"})
    elif not all(key in req for key in
                 ["login", "password", "email", "role_id"]):
        return jsonify({"error": "Bad request"})
    else:
        user = User()
        user.login = req["login"]
        user.password = generate_password_hash(req["password"])
        user.email = req["email"]
        user.role_id = req["role_id"]
        return user


@blueprint.route("/api/chair")
def get_all_chairs():
    return jsonify(chair_list_resource.get())


@blueprint.route("/api/chair/<int:chair_id>")
def get_one_chair(chair_id):
    return jsonify(chair_resource.get(chair_id))


@blueprint.route("/api/chair", methods=["POST"])
def create_chair():
    try:
        return jsonify(chair_resource.post(check_request_chair(request)))
    except:
        return jsonify(check_request_chair(request))


@blueprint.route("/api/chair/<int:chair_id>", methods=["PUT"])
def edit_chair(chair_id):
    try:
        return jsonify(chair_resource.put(chair_id, check_request_chair(request)))
    except:
        return jsonify(check_request_chair(request))


@blueprint.route("/api/chair/<int:chair_id>", methods=["DELETE"])
def delete_chair(chair_id):
    return jsonify(chair_resource.delete(chair_id))


@blueprint.route("/api/cinema")
def get_all_cinemas():
    return jsonify(cinema_list_resource.get())


@blueprint.route("/api/cinema/<int:cinema_id>")
def get_one_cinema(cinema_id):
    return jsonify(cinema_resource.get(cinema_id))


@blueprint.route("/api/cinema", methods=["POST"])
def create_cinema():
    try:
        return jsonify(cinema_resource.post(check_request_cinema(request.json)))
    except:
        return jsonify(check_request_cinema(request.json))


@blueprint.route("/api/cinema/<int:cinema_id>", methods=["PUT"])
def edit_cinema(cinema_id):
    try:
        return jsonify(cinema_resource.put(cinema_id, check_request_cinema(request.json)))
    except:
        return jsonify(check_request_cinema(request.json))


@blueprint.route("/api/cinema/<int:cinema_id>", methods=["DELETE"])
def delete_cinema(cinema_id):
    return jsonify(cinema_resource.delete(cinema_id))


@blueprint.route("/api/cost")
def get_all_cost():
    return jsonify(cost_list_resource.get())


@blueprint.route("/api/cost/<int:cost_id>")
def get_one_cost(cost_id):
    return jsonify(cost_resource.get(cost_id))


@blueprint.route("/api/cost", methods=["POST"])
def create_cost():
    try:
        return jsonify(cost_resource.post(check_request_cost(request.json)))
    except:
        return jsonify(check_request_cost(request.json))


@blueprint.route("/api/cost/<int:cost_id>", methods=["PUT"])
def edit_cost(cost_id):
    try:
        return jsonify(cost_resource.put(cost_id, check_request_cost(request.json)))
    except:
        return jsonify(check_request_cost(request.json))


@blueprint.route("/api/cost/<int:cost_id>", methods=["DELETE"])
def delete_cost(cost_id):
    return jsonify(cost_resource.delete(cost_id))


@blueprint.route("/api/film")
def get_all_film():
    return jsonify(film_list_resource.get())


@blueprint.route("/api/film/<int:film_id>")
def get_one_film(film_id):
    return jsonify(film_resource.get(film_id))


@blueprint.route("/api/film", methods=["POST"])
def create_film():
    try:
        return jsonify(film_resource.post(check_request_film(request.json)))
    except:
        return jsonify(check_request_film(request.json))


@blueprint.route("/api/film/<int:film_id>", methods=["PUT"])
def edit_film(film_id):
    try:
        return jsonify(film_resource.put(film_id, check_request_film(request.json)))
    except:
        return jsonify(check_request_film(request.json))


@blueprint.route("/api/film/<int:film_id>", methods=["DELETE"])
def delete_film(film_id):
    return jsonify(film_resource.delete(film_id))


@blueprint.route("/api/genre")
def get_all_genre():
    return jsonify(genre_list_resource.get())


@blueprint.route("/api/genre/<int:genre_id>")
def get_one_genre(genre_id):
    return jsonify(genre_resource.get(genre_id))


@blueprint.route("/api/hall")
def get_all_halls():
    return jsonify(hall_list_resource.get())


@blueprint.route("/api/hall/<int:hall_id>")
def get_one_hall(hall_id):
    return jsonify(hall_resource.get(hall_id))


@blueprint.route("/api/hall", methods=["POST"])
def create_hall():
    try:
        return jsonify(hall_resource.post(check_request_hall(request.json)))
    except:
        return jsonify(check_request_hall(request.json))


@blueprint.route("/api/hall/<int:hall_id>", methods=["PUT"])
def edit_hall(hall_id):
    try:
        return jsonify(hall_resource.put(hall_id, check_request_hall(request.json)))
    except:
        return jsonify(check_request_hall(request.json))


@blueprint.route("/api/hall/<int:hall_id>", methods=["DELETE"])
def delete_hall(hall_id):
    return jsonify(hall_resource.delete(hall_id))


@blueprint.route("/api/record")
def get_all_records():
    return jsonify(record_list_resource.get())


@blueprint.route("/api/record/<int:record_id>")
def get_one_record(record_id):
    return jsonify(record_resource.get(record_id))


@blueprint.route("/api/record", methods=["POST"])
def create_record():
    try:
        return jsonify(record_resource.post(check_request_record(request.json)))
    except:
        return jsonify(check_request_record(request.json))


@blueprint.route("/api/record/<int:record_id>", methods=["PUT"])
def edit_record(record_id):
    try:
        return jsonify(record_resource.put(record_id, check_request_record(request.json)))
    except:
        return jsonify(check_request_record(request.json))


@blueprint.route("/api/record/<int:record_id>", methods=["DELETE"])
def delete_record(record_id):
    return jsonify(record_resource.delete(record_id))


@blueprint.route("/api/record_type")
def get_all_record_types():
    return jsonify(record_type_list_resource.get())


@blueprint.route("/api/record_type/<int:record_type_id>")
def get_one_record_type(record_type_id):
    return jsonify(record_type_resource.get(record_type_id))


@blueprint.route("/api/role")
def get_all_roles():
    return jsonify(role_list_resource.get())


@blueprint.route("/api/role/<int:role_id>")
def get_one_role(role_id):
    return jsonify(role_resource.get(role_id))


@blueprint.route("/api/session")
def get_all_sessions():
    return jsonify(session_list_resource.get())


@blueprint.route("/api/session/<int:session_id>")
def get_one_session(session_id):
    return jsonify(session_resource.get(session_id))


@blueprint.route("/api/session", methods=["POST"])
def create_session():
    try:
        return jsonify(session_resource.post(check_request_session(request.json)))
    except:
        return jsonify(check_request_session(request.json))


@blueprint.route("/api/session/<int:session_id>", methods=["PUT"])
def edit_session(session_id):
    try:
        return jsonify(session_resource.put(session_id, check_request_session(request.json)))
    except:
        return jsonify(check_request_session(request.json))


@blueprint.route("/api/session/<int:session_id>", methods=["DELETE"])
def delete_session(session_id):
    return jsonify(session_resource.delete(session_id))


@blueprint.route("/api/ticket")
def get_all_tickets():
    return jsonify(ticket_list_resource.get())


@blueprint.route("/api/ticket/<int:ticket_id>")
def get_one_ticket(ticket_id):
    return jsonify(ticket_resource.get(ticket_id))


@blueprint.route("/api/ticket", methods=["POST"])
def create_ticket():
    try:
        return jsonify(ticket_resource.post(check_request_ticket(request.json)))
    except:
        return jsonify(check_request_ticket(request.json))


@blueprint.route("/api/ticket/<int:ticket_id>", methods=["PUT"])
def edit_ticket(ticket_id):
    try:
        return jsonify(ticket_resource.put(ticket_id, check_request_ticket(request.json)))
    except:
        return jsonify(check_request_ticket(request.json))


@blueprint.route("/api/ticket/<int:ticket_id>", methods=["DELETE"])
def delete_ticket(ticket_id):
    return jsonify(ticket_resource.delete(ticket_id))


@blueprint.route("/api/user")
def get_all_users():
    return jsonify(user_list_resource.get())


@blueprint.route("/api/user/<int:user_id>")
def get_one_user(user_id):
    return jsonify(user_resource.get(user_id))


@blueprint.route("/api/user", methods=["POST"])
def create_user():
    try:
        return jsonify(user_resource.post(check_request_user(request.json)))
    except:
        return jsonify(check_request_user(request.json))


@blueprint.route("/api/user/<int:user_id>", methods=["PUT"])
def edit_user(user_id):
    try:
        return jsonify(user_resource.put(user_id, check_request_user(request.json)))
    except:
        return jsonify(check_request_user(request.json))


@blueprint.route("/api/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return jsonify(user_resource.delete(user_id))
