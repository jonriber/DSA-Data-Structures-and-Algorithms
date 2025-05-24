# Description: Exercise 2 - Computer builder
# Build a ComputerBuilder that creates desktops or laptops with CPU, RAM, storage, and GPU. Some components are 
# optional.

class Computer:
  def __init__(self):
    self.cpu = None
    self.ram = None
    self.storage = None
    self.gpu = None
    self.is_laptop = False
  def __str__(self):
    return (
      f"Computer:\n"
      f"CPU: {self.cpu}\n"
      f"RAM: {self.ram}\n"
      f"Storage: {self.storage}\n"
      f"GPU: {self.gpu}\n"
      f"Type: {'Laptop' if self.is_laptop else 'Desktop'}"
    )

if __name__ == "__main__":
  pass