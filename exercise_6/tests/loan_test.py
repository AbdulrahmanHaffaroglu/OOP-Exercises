from library_management_system.models import Book, Library, Member


class TestLoan:

    # -------------------------
    # Object creation
    # -------------------------

    def test_creation_links_member_book_and_library(self):
        # Arrange
        library = Library()
        member = Member("M001", "John")
        book = Book("978-1-23456-789-0", "Python Basics", "Alice Smith", 2020)
        library.add_book(book)
        library.register_member(member)

        # Act
        loan = library.borrow_book(book, member)

        # Assert
        assert loan.member is member
        assert loan.book is book
        assert loan in member._loans
        assert loan in library.loans
        assert loan.is_returned() is False

    # -------------------------
    # Return behavior
    # -------------------------

    def test_returns_are_recorded(self):
        # Arrange
        library = Library()
        member = Member("M001", "John")
        book = Book("978-1-23456-789-0", "Python Basics", "Alice Smith", 2020)
        library.add_book(book)
        library.register_member(member)
        loan = library.borrow_book(book, member)

        # Act
        library.return_book(book, member)

        # Assert
        assert loan.is_returned() is True
        assert loan._returned_date is not None
