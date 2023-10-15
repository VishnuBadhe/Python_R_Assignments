# Que1.
#  Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
#  Write a python program to Create a child class Bus that will inherit all of the variables and methods of the Vehicle class.


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_vehicle_details(self):
        print(f"max_speed = {self.max_speed}")
        print(f"mileage = {self.mileage}")


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, colour, fuel ):
        Vehicle.__init__(self, max_speed, mileage)
        self.colour = colour
        self.fuel = fuel

    def print_bus_details(self):
        Vehicle.print_vehicle_details(self)
        print(f"colour = {self.colour}")
        print(f"fuel = {self.fuel}")

print(f"---Vehicle Details---")
v = Vehicle(90, 30)
v.print_vehicle_details()
# print(f"v = {v.__dict__}")

print()

print(f'---Bus Details---')
b = Bus(90, 30, 'red', 'diesel')
b.print_bus_details()
# print(f"b = {b.__dict__}")




