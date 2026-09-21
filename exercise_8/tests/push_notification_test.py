from notification_system.models.push_notification import PushNotification


class TestPushNotification:
    def test_creation(self):
        push = PushNotification('device-123')

        assert push.device_id == 'device-123'

    def test_send_prints_message(self, capsys):
        push = PushNotification('device-123')

        push.send('hello', user='Alice')

        captured = capsys.readouterr()
        assert 'device-123' in captured.out
        assert 'hello' in captured.out
