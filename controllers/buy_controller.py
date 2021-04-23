from services.buy_service import BuyService


class BuyResource:
    buy_service = BuyService()

    def buy(self, ticket_id: int):
        self.buy_service.buy(ticket_id)
