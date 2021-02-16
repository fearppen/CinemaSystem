from services.i_authorise_adapter import IAuthoriseAdapter


class SignUpAdapter(IAuthoriseAdapter):
    def get_authorisation_data(self, login: str, password: str):
        pass
