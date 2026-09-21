import pytest

from notification_system.models.user import User


class TestUser:
    def test_creation(self):
        user = User(
            name='Hakan',
            email='hakan@gmail.com',
            phone_number='905075981232',
            password='Hkkn123',
            device_id='Hakan Galaxy A12'
        )

        assert user.name == 'Hakan'
        assert user.email == 'hakan@gmail.com'
        assert user.phone_number == '905075981232'
        assert user.device_id == 'Hakan Galaxy A12'

    def test_place_order_adds_order_and_notifies(self, capsys):
        user = User(
            name='Hakan',
            email='hakan@gmail.com',
            phone_number='905075981232',
            password='Hkkn123',
            device_id='Hakan Galaxy A12'
        )

        user.place_order('3 books')

        assert '3 books' in user.orders
        captured = capsys.readouterr()
        assert 'your order: 3 books has been successfully placed' in captured.out

    def test_cancel_order_removes_order(self, capsys):
        user = User(
            name='Hakan',
            email='hakan@gmail.com',
            phone_number='905075981232',
            password='Hkkn123',
            device_id='Hakan Galaxy A12'
        )

        user.place_order('2 books')
        user.cancel_order('2 books')

        assert '2 books' not in user.orders
        captured = capsys.readouterr()
        assert 'your order: 2 books has been successfully removed' in captured.out

    def test_duplicate_order_raises_value_error(self):
        user = User(
            name='Hakan',
            email='hakan@gmail.com',
            phone_number='905075981232',
            password='Hkkn123',
            device_id='Hakan Galaxy A12'
        )

        user.place_order('3 books')

        with pytest.raises(ValueError):
            user.place_order('3 books')

    def test_cancel_missing_order_raises_value_error(self):
        user = User(
            name='Hakan',
            email='hakan@gmail.com',
            phone_number='905075981232',
            password='Hkkn123',
            device_id='Hakan Galaxy A12'
        )

        with pytest.raises(ValueError):
            user.cancel_order('missing item')

    def test_change_password_updates_password(self, capsys):
        user = User(
            name='Hakan',
            email='hakan@gmail.com',
            phone_number='905075981232',
            password='Hkkn123',
            device_id='Hakan Galaxy A12'
        )

        user.change_password('NewPass123')

        assert user.password == 'NewPass123'
        captured = capsys.readouterr()
        assert 'your password has been changed successfully' in captured.out

    def test_change_password_same_as_old_raises_value_error(self):
        user = User(
            name='Hakan',
            email='hakan@gmail.com',
            phone_number='905075981232',
            password='Hkkn123',
            device_id='Hakan Galaxy A12'
        )

        with pytest.raises(ValueError):
            user.change_password('Hkkn123')

    def test_send_email_uses_target_user(self, capsys):
        sender = User(
            name='Hakan',
            email='hakan@gmail.com',
            phone_number='905075981232',
            password='Hkkn123',
            device_id='Hakan Galaxy A12'
        )
        receiver = User(
            name='Ali',
            email='ali@gmail.com',
            phone_number='905000000000',
            password='Ali123',
            device_id='Ali Phone'
        )

        sender.send_email('hello', receiver)

        captured = capsys.readouterr()
        assert 'hello' in captured.out
        assert 'Ali' in captured.out

    def test_send_message_uses_target_user(self, capsys):
        sender = User(
            name='Hakan',
            email='hakan@gmail.com',
            phone_number='905075981232',
            password='Hkkn123',
            device_id='Hakan Galaxy A12'
        )
        receiver = User(
            name='Ali',
            email='ali@gmail.com',
            phone_number='905000000000',
            password='Ali123',
            device_id='Ali Phone'
        )

        sender.send_message('hello', receiver)

        captured = capsys.readouterr()
        assert 'hello' in captured.out
        assert 'Ali' in captured.out
