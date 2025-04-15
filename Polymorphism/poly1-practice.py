
#Shape Area Calculator (Polymorphism with Method Overriding)
# In this example, we define a base class `Shape` with a method `area()`.
# We then create two subclasses, `Rectangle` and `Circle`, that override the `area()` method to calculate their respective areas.
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Practice:
shapes = [Rectangle(10, 5), Circle(7)]
for shape in shapes:
    print("Area:", shape.area())




#Create a Vehicle class. Subclasses Bike, Car, Bus should override max_speed() method.

class Vehicle:
    def max_speed(self):
        return 0

class Bike(Vehicle):
    def max_speed(self):
        return 100

class Car(Vehicle):
    def max_speed(self):
        return 500

class Bus(Vehicle):
    def max_speed(self):
        return 800

vehicles = [Vehicle(),Bike(),Car(),Bus()]

for vehicle in vehicles:
    print(vehicle.max_speed())





