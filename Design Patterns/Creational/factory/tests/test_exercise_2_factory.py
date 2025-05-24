import pytest
from ..exercise_2_factory import MessageFactory, EmailMessage, SMSMessage, PushNotification, Message

class TestMessageFactory:
  def test_create_email_message(self):
    factory = MessageFactory()
    message = factory.create_message("Email")
    assert isinstance(message, EmailMessage)
  
  def test_create_sms_message(self):
    factory = MessageFactory()
    message = factory.create_message("SMS")
    assert isinstance(message, SMSMessage)
  
  def test_create_push_notification(self):
    factory = MessageFactory()
    message = factory.create_message("Push")
    assert isinstance(message, PushNotification)
  
  def test_invalid_channel(self):
    factory = MessageFactory()
    with pytest.raises(ValueError):
      factory.create_message("InvalidChannel")