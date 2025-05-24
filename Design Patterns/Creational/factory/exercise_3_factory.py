# Description: Create a VehicleFactory that returns different types of Vehicle (Car, Bike, Truck) depending on the 
# user input. Each type should accept parameters like color and wheels during instantiation.

# Requirements:
# 1. The factory must accept the vehicle type and initialization parameters.
# 2. All classes must implement a description() method.

class Vehicle:
  def __init__(self, color:str, wheels:int):
    self.color = color
    self.wheels = wheels
    
  def description(self):
    raise NotImplementedError("Subclasses must implement this method")
    
class Car(Vehicle):
  
  def description(self):
    return f"Car color: {self.color}, Car Wheels: {self.wheels}"

class Bike(Vehicle):
  def description(self):
    return f"Bike color: {self.color}, Bike Wheels: {self.wheels}"
  
class Truck(Vehicle):
  def description(self):
    return f"Truck color: {self.color}, Truck Wheels: {self.wheels}"

class VehicleFactory:
  vehicle_registry = {
    "Car": Car,
    "Bike": Bike,
    "Truck": Truck
  }
  
  def create_vehicle(self, vehicle_type, vehicle_color, vehicle_wheels) -> Vehicle:
    if vehicle_type not in self.vehicle_registry:
      raise ValueError(f"Unknown vehicle type: {vehicle_type}")
    vehicle_class = self.vehicle_registry[vehicle_type]
    return vehicle_class(vehicle_color, vehicle_wheels)

if __name__ == "__main__":
  pass
