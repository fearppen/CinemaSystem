from flask import Flask, render_template
from flask_login import current_user, LoginManager

from controllers.login_controller import LoginResource
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
            return render_template("index.html", name_page="Билетная система")
    return render_template("authorisation.html", type_page="Авторизация",
                           name_page="Авторизация", form=form)


@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        return render_template("registration.html", name_page="Регистрация",
                               type_page="Регистрация", message="", form=form)
    return render_template("registration.html", type_page="Регистрация",
                           name_page="Регистрация", form=form)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    db_session.global_init("./db/system.db")
    app.run(port=8080, host="localhost")
