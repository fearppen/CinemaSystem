from abc import ABC, abstractmethod


class IAuthoriseAdapter(ABC):
    @abstractmethod
    def get_authorisation_data(self, login: str, password: str):
        pass
