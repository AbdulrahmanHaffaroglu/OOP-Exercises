import pytest

from library_management_system.models import Book, Library, Member


class TestLibrary:

    # -------------------------
    # Book and member registration
    # -------------------------

    def test_add_book_and_register_member(self):
        # Arrange
        library = Library()
        book = Book("978-1-23456-789-0", "Python Basics", "Alice Smith", 2020)
        member = Member("M001", "John")

        # Act
        library.add_book(book)
        library.register_member(member)

        # Assert
        assert book in library.books
        assert member in library.members

    # -------------------------
    # Borrowing and returning
    # -------------------------

    def test_can_borrow_and_return_book(self):
        # Arrange
        library = Library()
        member = Member("M001", "John")
        book = Book("978-1-23456-789-0", "Python Basics", "Alice Smith", 2020)
        library.add_book(book)
        library.register_member(member)

        # Act
        loan = library.borrow_book(book, member)
        library.return_book(book, member)

        # Assert
        assert loan.book is book
        assert book.status_getter() == "available"
        assert book not in member._borrowed_books

    def test_rejects_duplicate_borrow(self):
        # Arrange
        library = Library()
        member = Member("M001", "John")
        book = Book("978-1-23456-789-0", "Python Basics", "Alice Smith", 2020)
        library.add_book(book)
        library.register_member(member)
        library.borrow_book(book, member)

        # Act / Assert
        with pytest.raises(ValueError):
            library.borrow_book(book, member)

    def test_rejects_more_than_three_books(self):
        # Arrange
        library = Library()
        member = Member("M001", "John")
        books = [
            Book("978-1-23456-789-0", "Book 1", "Alice", 2020),
            Book("978-1-23456-789-1", "Book 2", "Alice", 2021),
            Book("978-1-23456-789-2", "Book 3", "Alice", 2022),
            Book("978-1-23456-789-3", "Book 4", "Alice", 2023),
        ]

        for book in books:
            library.add_book(book)
        library.register_member(member)

        # Act
        for book in books[:3]:
            library.borrow_book(book, member)

        # Assert
        with pytest.raises(ValueError):
            library.borrow_book(books[3], member)

    def test_rejects_return_of_book_not_borrowed(self):
        # Arrange
        library = Library()
        member = Member("M001", "John")
        book = Book("978-1-23456-789-0", "Python Basics", "Alice Smith", 2020)
        library.add_book(book)
        library.register_member(member)

        # Act / Assert
        with pytest.raises(ValueError):
            library.return_book(book, member)

    def test_rejects_return_by_wrong_member(self):
        # Arrange
        library = Library()
        owner = Member("M001", "John")
        other_member = Member("M002", "Mary")
        book = Book("978-1-23456-789-0", "Python Basics", "Alice Smith", 2020)
        library.add_book(book)
        library.register_member(owner)
        library.register_member(other_member)
        library.borrow_book(book, owner)

        # Act / Assert
        with pytest.raises(ValueError):
            library.return_book(book, other_member)

    # -------------------------
    # Search behavior
    # -------------------------

    def test_find_books_by_title(self):
        # Arrange
        library = Library()
        book_1 = Book("978-1-23456-789-0", "Python Basics", "Alice Smith", 2020)
        book_2 = Book("978-1-23456-789-1", "Advanced Python", "Alice Smith", 2021)
        library.add_book(book_1)
        library.add_book(book_2)

        # Act
        result = library.find_book_title("Python Basics")

        # Assert
        assert result == [
            (
                "978-1-23456-789-0",
                "Python Basics",
                "Alice Smith",
                2020,
                "available",
            )
        ]

    def test_find_books_by_author(self):
        # Arrange
        library = Library()
        book_1 = Book("978-1-23456-789-0", "Python Basics", "Alice Smith", 2020)
        book_2 = Book("978-1-23456-789-1", "Advanced OOP", "Alice Smith", 2021)
        library.add_book(book_1)
        library.add_book(book_2)

        # Act
        result = library.find_book_author("Alice Smith")

        # Assert
        assert result == [
            (
                "978-1-23456-789-0",
                "Python Basics",
                "Alice Smith",
                2020,
                "available",
            ),
            (
                "978-1-23456-789-1",
                "Advanced OOP",
                "Alice Smith",
                2021,
                "available",
            ),
        ]

    # -------------------------
    # Invalid library operations
    # -------------------------

    def test_rejects_unregistered_member_on_borrow(self):
        # Arrange
        library = Library()
        member = Member("M999", "Ghost")
        book = Book("978-1-23456-789-0", "Python Basics", "Alice Smith", 2020)
        library.add_book(book)

        # Act / Assert
        with pytest.raises(ValueError):
            library.borrow_book(book, member)

    def test_rejects_invalid_book_year_on_library_addition(self):
        # Arrange
        library = Library()

        # Act / Assert
        with pytest.raises(ValueError):
            library.add_book(Book("978-1-23456-789-0", "Bad Book", "Alice", 3000))
