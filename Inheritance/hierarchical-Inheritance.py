# Hierarchical Inheritance occurs when multiple child classes inherit from the same parent class.

#            [Parent Class]
#            /      |      \
#  [Child1]   [Child2]   [Child3]


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")

# Objects of Dog and Cat
d = Dog("Buddy")
d.eat()
d.bark()

c = Cat("Whiskers")
c.eat()
c.meow()



# Shape Area Calculator

# Parent: Shape

# Child1: Circle (radius)

# Child2: Rectangle (length, width)

class Shape:
    def __init__(self,name):
        self.name = name
    
    def display(self):
        print(f'shape is {self.name}')
        

class Circle(Shape):
    def __init__(self,radius,name):
        super().__init__(name)
        self.radius = radius
    
    def calculate_radius(self):
        area_circle = 3.14*self.radius**2
        print(f'Area of circle - {area_circle}')


# Child class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(f"Area of the rectangle {self.length} x {self.width} is {area:.2f}")

c1 = Circle(5,'circle')
c1.calculate_radius()
r1 = Rectangle(4, 6)
r1.display()
r1.area()