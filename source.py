from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_required, logout_user, login_user
from werkzeug.security import check_password_hash

from controllers.cinemas_controller import CinemasListResources
from controllers.genre_controller import GenreListResources
from controllers.registration_controller import RegistrationResource
from domain import db_session
from domain.user import User
from forms.authorisation_form import AuthorisationForm
from forms.filter_films import FilterFilmForm
from forms.registration_form import RegistrationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandex_lyceum_secret_key"

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    cinemas_resource = CinemasListResources()
    cinemas = cinemas_resource.get()["cinemas"]
    genres_resources = GenreListResources()
    genres = genres_resources.get()["genres"]
    filter_film_form = FilterFilmForm()
    filter_film_form.genre.choices = [(genre["id"], genre["title"]) for genre in genres]
    filter_film_form.cinema.choices = [(cinema["id"], cinema["title"]) for cinema in cinemas]
    if filter_film_form.validate_on_submit():
        print(filter_film_form.cinema.data)
        print(filter_film_form.cinema.data)
        #return redirect(f"/filter_by/{filter_film_form.cinema.data}, {filter_film_form.cinema.data}")
    return render_template("index.html", name_page="Основная", filter_film_form=filter_film_form)


@app.route("/filter_by/<int:genre>,<int:cinema>", methods=["GET", "POST"])
def filter_films(cinema, genre):
    pass


@app.route("/authorisation", methods=["GET", "POST"])
def authorisation():
    form = AuthorisationForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        else:
            return render_template("authorisation.html", name_page="Авторизация",
                                   type_page="Авторизация", form=form)
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
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    db_session.global_init("./db/system.db")
    app.run(port=8080, host="localhost")
