from notification_system.models.email import Email


class TestEmail:
    def test_creation(self):
        email = Email('user@example.com')

        assert email.email == 'user@example.com'

    def test_send_without_user_prints_message(self, capsys):
        email = Email('user@example.com')

        email.send('hello')

        captured = capsys.readouterr()
        assert 'user@example.com' in captured.out
        assert 'hello' in captured.out

    def test_send_with_user_prints_recipient(self, capsys):
        email = Email('user@example.com')

        email.send('hello', user='Alice')

        captured = capsys.readouterr()
        assert 'user@example.com' in captured.out
        assert 'hello' in captured.out
        assert 'Alice' in captured.out
