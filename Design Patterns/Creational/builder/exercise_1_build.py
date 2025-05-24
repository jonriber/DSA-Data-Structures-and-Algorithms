# Description: Build a class to construct a Sandwich object with optional ingredients: bread, meat, cheese, 
# vegetables, sauce.

class Sandwich:
  def __init__(self):
    self.bread = None
    self.meat = None
    self.cheese = None
    self.vegetables = []
    self.sauce = None
    
  def __str__(self):
    return(
      f"Sandwich with:\n"
      f"Bread: {self.bread}\n"
      f"Meat: {self.meat}\n"
      f"Cheese: {self.cheese}\n"
      f"Vegetables: {', '.join(self.vegetables)}\n"
      f"Sauce: {self.sauce}"
    )

class SandwichBuilder:
  def __init__(self):
    self.sandwich = Sandwich()
  def set_bread(self, bread: str):
    self.sandwich.bread = bread
    return self
  def set_meat(self, meat: str):
    self.sandwich.meat = meat
    return self
  def set_cheese(self, cheese: str):
    self.sandwich.cheese = cheese
    return self
  def add_vegetable(self, vegetable: str):
    self.sandwich.vegetables.append(vegetable)
    return self
  def set_sauce(self, sauce: str):
    self.sandwich.sauce = sauce
    return self
  def build(self):
    if not self.sandwich.bread:
      raise ValueError("Bread must be set")
    return self.sandwich
  
if __name__ == "__main__":
  # Sandwich builder usage example
  
  builder = SandwichBuilder()
  
  sandwich = (
    builder
    .set_bread("Whole Wheat")
    .set_meat("Turkey")
    .set_cheese("Swiss")
    .add_vegetable("Lettuce")
    .add_vegetable("Tomato")
    .set_sauce("Mustard")
    .build()
  )
  
  print(sandwich)
# Output:
# Sandwich with:
# Bread: Whole Wheat
# Meat: Turkey
# Cheese: Swiss
# Vegetables: Lettuce, Tomato
# Sauce: Mustard
# This code defines a Sandwich class and a SandwichBuilder class that allows for the construction of a Sandwich object
# with various optional ingredients. The builder pattern is used to create a flexible and readable way to 
# build the sandwich.