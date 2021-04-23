from domain import db_session
from requests import get, post

db_session.global_init("../db/system.db")
x = post("http://mycinemasystem.herokuapp.com/", data={"row": 1, "place": 1, "hall_id": 1})
print(x)
