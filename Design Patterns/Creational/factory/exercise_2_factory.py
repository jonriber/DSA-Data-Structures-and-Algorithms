# Factory Exercise 2
# Description: Build a MessageFactory that creates different types of message objects (EmailMessage, 
# SMSMessage, PushNotification) based on the channel. Each message class must implement a send() method.

# Requirements: 
# 1. Use inheritance or duck typing.
# 2. Simulate sending by printing Sending {message}.
# 3. Bonus: Use a dictionary to map string keys to classes.
class Message:
  def send(self):
    pass

class EmailMessage(Message):
  def send(self):
    print("Sending Email Message")
    
class SMSMessage(Message):
  def send(self):
    print("Sending SMS Message")
    
class PushNotification(Message):
  def send(self):
    print("Sending Push Notification")

class MessageFactory:
  def create_message(self, channel: str) -> Message:
    if channel == "Email":
      return EmailMessage()
    elif channel == "SMS":
      return SMSMessage() 
    elif channel == "Push":
      return PushNotification()
    else:
      raise ValueError("Unknown message channel")
    
  

if __name__ == "__main__":
  print("Factory Pattern Example")
  factory = MessageFactory()
  channels = ["Email", "SMS", "Push"]
  for channel in channels:
    message_instance = factory.create_message(channel)
    message_instance.send()
    
    
  

# to the one in Design%20Patterns/Creational/factory/exercise_2_factory.py