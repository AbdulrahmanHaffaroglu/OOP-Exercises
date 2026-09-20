class Book:

    def __init__(self, isbn, title, author, publication_year):
        if not isinstance(publication_year, int) or publication_year < 1000 or 2026 < publication_year:
            raise ValueError("this is not a valid publish year")

        self.isbn = isbn
        self.title = title
        self.author = author
        self._publication_year = publication_year
        self._status = "available"


    def status_setter(self, status):
        if self.status != 'available' and status == "borrowed":
            raise ValueError("you cant borrow a book if it's unavailable")

        self._status = status

    def status_getter(self):
        return self._status

    status = property(fset=status_setter, fget=status_getter)