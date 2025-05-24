# Factory Exercise 2
# Description: Build a MessageFactory that creates different types of message objects (EmailMessage, 
# SMSMessage, PushNotification) based on the channel. Each message class must implement a send() method.

# Requirements: 
# 1. Use inheritance or duck typing.
# 2. Simulate sending by printing Sending {message}.
# 3. Bonus: Use a dictionary to map string keys to classes.
class Message:
  
  def __init__(self, content: str):
    self.content = content
    
  def send(self):
    raise NotImplementedError("Subclasses must implement this method")

class EmailMessage(Message):
  def send(self):
    print("Sending Email Message:", self.content)
    
class SMSMessage(Message):
  def send(self):
    print("Sending SMS Message:", self.content)
    
class PushNotification(Message):
  def send(self):
    print("Sending Push Notification:", self.content)

class MessageFactory:
  
  _registry = {
    "Email": EmailMessage,
    "SMS": SMSMessage,
    "Push": PushNotification
  }
  
  @staticmethod
  def create_message(type_:str, content: str) -> Message:
    message_class = MessageFactory._registry.get(type_.lower())
    if not message_class:
      raise ValueError(f"Unknown message type: {type_}")
    return message_class(content)
    
  

if __name__ == "__main__":
  print("Factory Pattern Example")
  factory = MessageFactory()
  channels = ["Email", "SMS", "Push"]
  for channel in channels:
    message_instance = factory.create_message(channel)
    message_instance.send()
    
    
  

# to the one in Design%20Patterns/Creational/factory/exercise_2_factory.py