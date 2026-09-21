from notification_system.models.sms import SMS


class TestSMS:
    def test_creation(self):
        sms = SMS('905050000000')

        assert sms.phone_number == '905050000000'

    def test_send_without_user_prints_message(self, capsys):
        sms = SMS('905050000000')

        sms.send('hello')

        captured = capsys.readouterr()
        assert '905050000000' in captured.out
        assert 'hello' in captured.out

    def test_send_with_user_prints_recipient(self, capsys):
        sms = SMS('905050000000')

        sms.send('hello', user='Alice')

        captured = capsys.readouterr()
        assert '905050000000' in captured.out
        assert 'hello' in captured.out
        assert 'Alice' in captured.out
