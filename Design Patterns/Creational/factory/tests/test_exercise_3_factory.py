import pytest
from ..exercise_3_factory import Vehicle, VehicleFactory, Car, Truck, Bike

class TestVehicle:
  def test_vehicle_description(self):
    vehicle = Vehicle("red", 4)
    with pytest.raises(NotImplementedError):
      vehicle.description()
  
class TestCar:
  def test_car_description(self):
    car = Car("blue", 4)
    assert car.description() == "Car color: blue, Car Wheels: 4"

class TestBike:
  def test_bike_description(self):
    bike = Bike("green", 2)
    assert bike.description() == "Bike color: green, Bike Wheels: 2"
    
class TestTruck:
  def test_truck_description(self):
    truck = Truck("yellow", 6)
    assert truck.description() == "Truck color: yellow, Truck Wheels: 6"
    
class TestVehicleFactory:
  def test_create_car(self):
    factory = VehicleFactory()
    car = factory.create_vehicle("Car", "red", 4)
    assert isinstance(car, Car)
    assert car.description() == "Car color: red, Car Wheels: 4"
    
  def test_create_bike(self):
    factory = VehicleFactory()
    bike = factory.create_vehicle("Bike", "blue", 2)
    assert isinstance(bike, Bike)
    assert bike.description() == "Bike color: blue, Bike Wheels: 2"
    
  def test_create_truck(self):
    factory = VehicleFactory()
    truck = factory.create_vehicle("Truck", "green", 6)
    assert isinstance(truck, Truck)
    assert truck.description() == "Truck color: green, Truck Wheels: 6"
    
  def test_invalid_vehicle_type(self):
    factory = VehicleFactory()
    with pytest.raises(ValueError):
      factory.create_vehicle("InvalidVehicle", "red", 4)