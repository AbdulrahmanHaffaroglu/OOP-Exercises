'''
Build a Library Management System.

Requirements

The system must support:

Books
Members
Library
Loansa

Every Book has:

ISBN
Title
Author
Publication year
Availability status

A book must:

Be borrowable only when available.
Become unavailable when borrowed.
Become available when returned.
Reject invalid publication years.

Every Member has:

Member ID
Name
A collection of borrowed books

A member must:

Be able to borrow books.
Be able to return books.
Not be able to borrow the same book twice.
Not be able to borrow more than 3 books at once.

Every Loan represents:

A member
A book
Borrow date
Return date

A loan should:

Record the book's borrowing information.
Know whether the book has been returned.

The Library must:

Store books.
Store members.
Store loans.
Allow books to be added.
Allow members to be registered.
Process borrowing.
Process returning.
Find books by title.
Find books by author.


Business Rules
A book cannot be borrowed if it is already borrowed.
A member cannot borrow more than 3 books.
A member cannot borrow the same book twice.
A book cannot be returned if it wasn't borrowed.
A member cannot return a book borrowed by another member.
Invalid operations must not corrupt the library state.
A loan must preserve the relationship between the specific member and specific book involved in the transaction.


Your implementation must demonstrate:

Encapsulation
Composition
Association
Properties
Object interaction
Separation of responsibilities
State management
At least one use of @property
At least one use of a private/protected attribute


Create:

At least 5 books
At least 3 members
Multiple loans

Demonstrate:

Borrowing a book
Returning a book
Searching for books
A member reaching the 3-book limit
Attempting to borrow an unavailable book
Attempting to borrow the same book twice
Attempting to return a book belonging to another member
At least 5 invalid operations
'''

import datetime


class Library:

    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []



    def add_book(self, book):
        self.books.append(book)



    def register_member(self, member):
        self.members.append(member)



    def add_loan(self, loan):
        self.loans.append(loan)



    def borrow_book(self, book, member):
        if book.status_getter() == "borrowed":
            raise ValueError("this book is already borrowed by someone")
        
        if len(member._borrowed_books) == 3:
            raise ValueError("you cant borrow more than three books")
        
        for l in member._loans:
            if l.book == book:
                raise ValueError("you borrowed this before")

        
        member._borrowed_books.append(book)
        book.status_setter("borrowed")
        member.loan = Library.Loan(self, book)



    def return_book(self, book, member):
        if book.status_getter() == "available":
            raise ValueError("this book isn't borrowed by anyone")
        
        if book not in member._borrowed_books:
            raise ValueError("you dont have this book to return it")
        
        member._borrowed_books.remove(book)
        book.status_setter("available")


        for item in member._loans:
            if item.book == book:
                item._returned_date = datetime.datetime.now()



    def find_book_title(self, title):
        for book in self.books:
            if title == book.title:
                return book

        return None

    
    def find_book_author(self, author):
        for book in self.books:
            if author == book.author:
                return book
    
        return None


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
            self._status = status


        def status_getter(self):
            return self._status


        status = property(fset=status_setter, fget=status_getter)

    class Member:

        def __init__(self, member_id, name):
            self.member_id = member_id
            self.name = name
            self._borrowed_books = []
            self._loans = []



    class Loan:
        def __init__(self, member, book):
            self.member = member
            self.book = book
            self._borrow_date = datetime.datetime.now()
            self._returned_date = None

            member._loans.append(self)
            Library.add_loan(self)

        def is_returned(self):
            if not self._returned_date:
                return False

            return True



        
if __name__ == "__main__":
    pass