from notification_system.models.notification import Notification
from notification_system.models.email import Email
from notification_system.models.sms import SMS
from notification_system.models.push_notification import PushNotification


class TestNotification:
    def test_creation_stores_message_and_user(self):
        channels = [
            Email('test@example.com'),
            SMS('905050000000'),
            PushNotification('device-1')
        ]

        notification = Notification(channels, 'hello world', user='Alice')

        assert notification.channel_types == channels
        assert notification.message == 'hello world'
        assert notification.user == 'Alice'

    def test_send_sends_message_to_all_channels(self, capsys):
        channels = [
            Email('test@example.com'),
            SMS('905050000000'),
            PushNotification('device-1')
        ]

        notification = Notification(channels, 'hello world', user='Alice')
        notification.send()

        captured = capsys.readouterr()
        assert 'hello world' in captured.out
        assert 'test@example.com' in captured.out
        assert '905050000000' in captured.out
        assert 'device-1' in captured.out
        assert 'Alice' in captured.out

    def test_send_without_user_still_works(self, capsys):
        channels = [
            Email('test@example.com'),
            SMS('905050000000')
        ]

        notification = Notification(channels, 'hi there', user=None)
        notification.send()

        captured = capsys.readouterr()
        assert 'hi there' in captured.out
        assert 'test@example.com' in captured.out
        assert '905050000000' in captured.out
