from flask import Flask, redirect, render_template
from flask_login import LoginManager, login_user

from controllers.users_controller import UserResource
from domain import db_session
from domain.user import User
from forms.login_form import LoginForm
from forms.register_form import RegistrationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandex_lyceum_secret_key"

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id: int):
    return UserResource.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', name_page='Авторизация',
                               message="Неправильный логин или пароль", form=form)
    return render_template('login.html', name_page='Авторизация', form=form)


@app.route('/registration')
def registration():
    form = RegistrationForm()
    return render_template("registration.html", name_page="Регистрация", form=form)


if __name__ == "__main__":
    db_session.global_init("./db/system.db")
    app.run(port=8080, host="localhost")
