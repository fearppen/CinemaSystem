from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_required, logout_user, login_user
from werkzeug.security import check_password_hash

from controllers.login_controller import LoginResource
from controllers.logout_user_controller import LogoutUser
from controllers.registration_controller import RegistrationResource
from domain import db_session
from domain.user import User
from forms.authorisation_form import AuthorisationForm
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
    return render_template("index.html", name_page="Основная")


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
            return render_template("index.html", name_page="Основная")
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
