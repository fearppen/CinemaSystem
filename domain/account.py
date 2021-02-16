from domain.history import History


class Account:
    def __init__(self, login: str, password: str, history: History):
        self.login = login
        self.password = password
        self.history = history

    def get_login(self):
        return self.login

    def get_password(self):
        return self.password

    def get_history(self):
        return self.history

    def set_login(self, login: str):
        self.login = login

    def set_password(self, password: str):
        self.password = password

    def set_history(self, history: History):
        self.history = history
