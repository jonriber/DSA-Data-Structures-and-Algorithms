
class Product:
  
  def operation(self):
    pass
  
class ConcreteProductA(Product):
  
  def operation(self):
    return "Product A"
  
class ConcreteProductB(Product):
  
  def operation(self):
    return "Product B"
  
class ProductFactory:
  def create_product(self, type_:str) -> Product:
    if type_ == "A":
      return ConcreteProductA()
    elif type_ == "B":
      return ConcreteProductB()
    else:
      raise ValueError("Unknown product type")

if __name__ == "__main__":
  
  pass