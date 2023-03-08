from abc import ABC, abstractmethod

# Abstract Base Classes - https://docs.python.org/3/library/abc.html

# example of employing static typing in a Python
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        ...

class Car(Vehicle):
    def drive(self):
        print("drive a car on the road")

class Boat(Vehicle):
    def drive(self):
        print("drive a boat on the water")

class Plane(Vehicle):
    def fly(self):
        print("fly a plane in the air")

def drive_it(vehicle):
    vehicle.drive()


car = Car()
boat = Boat()
plane = Plane() # TypeError: Can't instantiate abstract class Plane with abstract method drive, compile-time error

drive_it(car)
drive_it(boat)
drive_it(plane) 