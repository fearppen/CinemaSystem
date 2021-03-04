from datetime import date

from data import db_session
from data.film import Film
from data.genre import Genre

db_session.global_init("db/system.db")
session = db_session.create_session()

genre_roman = Genre(title='Роман')
genre_fan = Genre(title='Фантастика')
session.add_all([genre_roman, genre_fan])

film1 = Film(title="film1", release_date=date.today(),
             director="Spielberg", duration="8h7m", genre=genre_roman)
film2 = Film(title="film2", release_date=date.today(),
             director="Schumaher", duration="8h7m", genre=genre_fan)
film3 = Film(title="film3", release_date=date.today(),
             director="Nolan", duration="8h7m", genre=genre_roman)
film4 = Film(title="film4", release_date=date.today(),
             director="Richi", duration="8h7m", genre=genre_fan)
session.add_all([film1, film2, film3, film4])

session.commit()
