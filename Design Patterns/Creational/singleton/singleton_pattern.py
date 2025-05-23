class Singleton:
  _instance = None
  
  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(Singleton, cls).__new__(cls)
    return cls._instance

if __name__ == '__main__':
  
  print("Singleton Pattern Example")
  
  # Singleton design pattern ensures a class has only one instance and provides a global point of access to it.
  class1 = Singleton()
  class2 = Singleton()
  class3 = Singleton()
  
  print(class1 is class2)  # True
  print(class2 is class3)  # True
  print(class1 is class3)  # True

  print("All instances are the same object.")
  print("Singleton pattern is implemented successfully.")


  

