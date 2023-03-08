# Duck-Typing: https://en.wikipedia.org/wiki/Duck_typing

# this is how Calculator and HistoryList are working
class Car:
    def drive(self):
        print("drive a car on the road")

class Boat:
    def drive(self):
        print("drive a boat on the water")

class Plane:
    def fly(self):
        print("fly a plane in the air")

def drive_it(vehicle):
    # duck typing - feature of dynamic typing (the types are resolved at runtime)
    vehicle.drive()


car = Car()
boat = Boat()
plane = Plane()

drive_it(car)
drive_it(boat)
# drive_it(plane) # AttributeError: 'Plane' object has no attribute 'drive', run-time error