import pytest

from notification_system.models.channel import Channel


class TestChannel:
    def test_channel_is_abstract(self):
        with pytest.raises(TypeError):
            Channel()
