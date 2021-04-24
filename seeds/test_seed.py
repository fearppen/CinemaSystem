from domain import db_session
from requests import get, post

db_session.global_init("../db/system.db")
#x = post("https://mycinemasystem.herokuapp.com/")
x = post("http://localhost:8080/api/chair")
print(x.text)
