import pytest

from library_management_system.models import Book


class TestBook:

    # -------------------------
    # Object creation
    # -------------------------

    def test_creation(self):
        # Arrange
        book = Book("978-1-23456-789-0", "Python Basics", "Alice Smith", 2020)

        # Assert
        assert book.isbn == "978-1-23456-789-0"
        assert book.title == "Python Basics"
        assert book.author == "Alice Smith"
        assert book._publication_year == 2020
        assert book.status_getter() == "available"

    # -------------------------
    # Properties / setters
    # -------------------------

    def test_status_property_can_change(self):
        # Arrange
        book = Book("978-1-23456-789-1", "OOP", "Bob Jones", 2021)

        # Act
        book.status = "borrowed"

        # Assert
        assert book.status_getter() == "borrowed"

    # -------------------------
    # Invalid inputs
    # -------------------------

    @pytest.mark.parametrize(
        "publication_year",
        [
            999,
            2027,
            0,
            -1,
            "2020",
        ],
    )
    def test_rejects_invalid_publication_years(self, publication_year):
        with pytest.raises(ValueError):
            Book("978-1-23456-789-2", "Invalid Year", "Alice Smith", publication_year)
