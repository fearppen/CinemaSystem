from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_required

from controllers.cinemas_controller import CinemasListResources
from controllers.genre_controller import GenreListResources
from controllers.login_controller import LoginResource
from controllers.logout_user_controller import LogoutUser
from controllers.registration_controller import RegistrationResource
from controllers.select_film_by_genre_and_cinema_controller import SelectFilmResource
from domain import db_session
from domain.user import User
from forms.authorisation_form import AuthorisationForm
from forms.filter_films_form import FilterFilmForm
from forms.registration_form import RegistrationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandex_lyceum_secret_key"

login_manager = LoginManager()
login_manager.init_app(app)


def filter_film_form_data():
    cinemas_resource = CinemasListResources()
    cinemas = cinemas_resource.get()["cinemas"]
    genres_resources = GenreListResources()
    genres = genres_resources.get()["genres"]
    filter_film_form = FilterFilmForm()
    filter_film_form.genre.choices = [(genre["id"], genre["title"]) for genre in genres]
    filter_film_form.cinema.choices = [(cinema["id"], cinema["title"]) for cinema in cinemas]
    return filter_film_form


# TODO: доделать
def filter_ticket_form_data():
    pass


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/", methods=["GET", "POST"])
def index():
    filter_film_form = filter_film_form_data()
    if filter_film_form.validate_on_submit():
        return redirect(
            f"/filter_by/{int(filter_film_form.cinema.data)},{int(filter_film_form.genre.data)}")
    return render_template("index.html", name_page="Основная", filter_film_form=filter_film_form)


@app.route("/filter_by/<int:cinema>,<int:genre>", methods=["GET", "POST"])
def filter_films(cinema, genre):
    filter_film_form = filter_film_form_data()
    resource = SelectFilmResource()
    films = resource.get(cinema, genre)["films"]
    if filter_film_form.validate_on_submit():
        return redirect(
            f"/filter_by/{int(filter_film_form.cinema.data)},{int(filter_film_form.genre.data)}")
    return render_template("index.html", name_page="Фильмы",
                           filter_film_form=filter_film_form, films=films)


# TODO: доделать
@app.route("/tickets/<int:cinema>,<int:film>", methods=["GET", "POST"])
def tickets(cinema, film):
    pass


# TODO: доделать
@app.route("/ticket/<int:ticket>", methods=["GET", "POST"])
def ticket(ticket):
    pass


# TODO: доделать
@app.route("/buy/<int:film>", methods=["GET", "POST"])
def buy(film):
    pass


# TODO: доделать
@app.route("/book/<int:film>", methods=["GET", "POST"])
def book(film):
    pass


@app.route("/authorisation", methods=["GET", "POST"])
def authorisation():
    form = AuthorisationForm()
    if form.validate_on_submit():
        resource = LoginResource()
        message = resource.login(form)
        if message:
            return render_template("authorisation.html", name_page="Авторизация",
                                   type_page="Авторизация", message=message, form=form)
        else:
            return redirect("/")
    return render_template("authorisation.html", type_page="Авторизация",
                           name_page="Авторизация", form=form)


@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        resource = RegistrationResource()
        message = resource.registration(form)
        if message:
            return render_template("registration.html", name_page="Регистрация",
                                   type_page="Регистрация", message=message, form=form)
        else:
            return redirect("/")
    return render_template("registration.html", type_page="Регистрация",
                           name_page="Регистрация", form=form)


@app.route("/logout")
@login_required
def logout():
    resource = LogoutUser()
    resource.logout()
    return redirect("/")


if __name__ == "__main__":
    db_session.global_init("./db/system.db")
    app.run(port=8080, host="localhost")
