from services.i_authorise_adapter import IAuthoriseAdapter


class SignInAdapter(IAuthoriseAdapter):
    def get_authorisation_data(self, login: str, password: str):
        pass
