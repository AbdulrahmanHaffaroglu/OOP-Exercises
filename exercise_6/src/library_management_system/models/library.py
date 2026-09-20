import datetime

from .loan import Loan 

class Library:

    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []


    def add_book(self, book):
        if book in self.books:
            raise ValueError("this book already exists in the library")
        
        self.books.append(book)

    def register_member(self, member):
        if member in self.members:
            raise ValueError("this member is already registered")
        
        self.members.append(member)

    def add_loan(self, loan):
        self.loans.append(loan)

    def borrow_book(self, book, member):
        if book not in self.books:
            raise ValueError("this book is not in the library")
        
        if member not in self.members:
            raise ValueError("this member is not registered")

        if book.status_getter() == "borrowed":
            raise ValueError("this book is already borrowed by someone")

        if len(member._borrowed_books) >= 3:
            raise ValueError("you cant borrow more than three books")

        if book in member._borrowed_books:
            raise ValueError("you borrowed this before")

        loan = Loan(member, book, self)
        member._borrowed_books.append(book)
        book.status_setter("borrowed")
        return loan

    def return_book(self, book, member):
        if book not in self.books:
            raise ValueError("this book is not in the library")

        if member not in self.members:
            raise ValueError("this member is not registered")

        if book.status_getter() == "available":
            raise ValueError("this book isn't borrowed by anyone")

        if book not in member._borrowed_books:
            raise ValueError("you dont have this book to return it")

        active_loan = None
        for item in member._loans:
            if item.book == book and not item.is_returned():
                active_loan = item
                break

        if active_loan is None:
            raise ValueError("this member does not have an active loan for this book")

        member._borrowed_books.remove(book)
        book.status_setter("available")
        active_loan._returned_date = datetime.datetime.now()
        return active_loan

    def find_book_title(self, title):
        matches = []
        for book in self.books:
            if title.lower() == book.title.lower():
                matches.append(
                    (
                        book.isbn,
                        book.title,
                        book.author,
                        book._publication_year,
                        book.status_getter(),
                    )
                )

        return matches if matches else None

    def find_book_author(self, author):
        matches = []
        for book in self.books:
            if author.lower() == book.author.lower():
                matches.append(
                    (
                        book.isbn,
                        book.title,
                        book.author,
                        book._publication_year,
                        book.status_getter(),
                    )
                )

        return matches if matches else None