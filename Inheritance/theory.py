#  What is Inheritance?
# Inheritance allows one class (child/subclass) to inherit the properties and methods of another class (parent/superclass).

# 🔑 Why use inheritance?
# To reuse code (don't repeat yourself!)

# To create a hierarchical relationship

# To extend or modify behaviors of parent class in child class



# class Parent:
#     # parent class methods and attributes

# class Child(Parent):
#     # child class inherits from Parent


#Example of Inheritance
class Animal:
    def eat(self):
        print("This animal eats food")

# Dog class inherits from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create a Dog object
d = Dog()
d.eat()   # Inherited from Animal
d.bark()  # Dog's own method


#Method overriding - 
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

c = Cat()
c.sound()   # Meow


#Super() keyword -
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()   # Call parent method
        print("Dog barks")

d = Dog()
d.sound()
