from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class FilterFilmForm(FlaskForm):
    genre = SelectField("Жанры", choices=[])
    cinema = SelectField("Кинотеатры", choices=[])
    submit = SubmitField('Показать')
