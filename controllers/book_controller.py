from services.book_service import BookService


class BookResource:
    book_service = BookService()

    def book(self, ticket_id: int):
        return self.book_service.book(ticket_id)
