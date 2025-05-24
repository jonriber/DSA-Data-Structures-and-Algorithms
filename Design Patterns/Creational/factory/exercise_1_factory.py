#Factory Simple example

# Description:
# Implement a simple ShapeFactory that creates shapes: Circle, Square, and Triangle. Each shape 
# must have a .draw() method that returns a string like "Drawing a Circle"

#requirements:
# 1. Use a base class Shape.
# 2. Subclasses: Circle, Square, Triangle.
# 3. The factory should return the correct subclass based on input.

class Shape:
  def draw(self):
    pass
  
class Circle(Shape):
  def draw(self):
    return "Drawing a Circle"
  
class Square(Shape):
  def draw(self):
    return "Drawing a Square"
  
class Triangle(Shape):
  def draw(self):
    return "Drawing a Triangle"

class ShapeFactory:
  def create_shape(self, shape_type:str) -> Shape:
    if shape_type == "Circle":
      return Circle()
    elif shape_type == "Square":
      return Square()
    elif shape_type == "Triangle":
      return Triangle()
    else:
      raise ValueError("Unknown shape type")

if __name__ == "__main__":
  print("Factory Pattern Example")
  factory = ShapeFactory()
  shapes = ["Circle", "Square", "Triangle"]
  for shape in shapes:
    shape_instance = factory.create_shape(shape)
    print(shape_instance.draw()) 