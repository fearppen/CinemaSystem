from flask import Flask, render_template

from domain import db_session
from forms.authorisation_form import AuthorisationForm
from forms.registration_form import RegistrationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandex_lyceum_secret_key"


@app.route("/authorisation", methods=["GET", "POST"])
def authorisation():
    form = AuthorisationForm()
    if form.validate_on_submit():
        return render_template("authorisation.html", name_page="Авторизация",
                               message="", form=form)
    return render_template("authorisation.html", name_page="Авторизация", form=form)


@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        return render_template("registration.html", name_page="Регистрация",
                               message="", form=form)
    return render_template("registration.html", name_page="Регистрация", form=form)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    db_session.global_init("./db/system.db")
    app.run(port=8080, host="localhost")
