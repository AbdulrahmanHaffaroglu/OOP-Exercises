from library_management_system.models import Member


class TestMember:

    # -------------------------
    # Object creation
    # -------------------------

    def test_creation(self):
        # Arrange
        member = Member("M001", "John")

        # Assert
        assert member.member_id == "M001"
        assert member.name == "John"
        assert member._borrowed_books == []
        assert member._loans == []
