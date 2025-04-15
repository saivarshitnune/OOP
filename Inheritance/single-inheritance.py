
### Single Inheritance
# Basic Animal Class
# Create a Parent class Animal with a method make_sound().
# Create a Dog class that inherits from Animal and has its own method bark().

class Vechile:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print(f'{self.brand} Vechile is started')

class Car(Vechile):
    def drive(self):
        print(f'{self.brand} can drive a car')


c1 = Car('Benz')
c1.drive()
c1.start()



###Super key word
# Student Report System
# Create a class Person with attributes name and age.
# Create a subclass Student that adds attributes grade and school.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):  # Student is a subclass of Person
    def __init__(self, name, age, grade, school):
        super().__init__(name, age)  #Passing variables to the parent class
        self.grade = grade
        self.school = school

# Create an object of Student
s1 = Student("John", 16, "10th", "XYZ High School")
p1=Person()

print(s1.name)  # From Person class
print(s1.age)   # From Person class
print(s1.grade) # From Student class
print(s1.school) # From Student class
print(p1.name)
print(p1.age)

# ✅ Why super() is used:
# Instead of re-writing code like self.name = name and self.age = age again in the child class,
# we use super().__init__(name, age) to call the parent class constructor,
# which already knows how to set those values.



#Library Membership System
# Create a base class Member with name, membership_id.

# Create a subclass PremiumMember with an additional attribute benefits.

# Use super() to set values from the parent.

# Create a method to display all details.

class Member:
    def __init__(self,name,membership_id):
        self.name = name
        self.membership_id = membership_id
    
class PremiumMember(Member):
    def __init__(self,name,membership_id,benefits):
        self.benefits = benefits
        super().__init__(name,membership_id)
    
    def display(self):
        print(self.benefits)
        print(self.membership_id)
        print(self.name)
        
p1 = PremiumMember('sai',12908,'ai books')
p1.display()




# Animal Sound Game
# Class Animal with name, species.

# Subclass Dog with a method make_sound() that says "Woof!".

# Subclass Cat with a method make_sound() that says "Meow!".

# Use super() where appropriate.

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
class Dog(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)
    
    def make_sound(self):
        print('woof')

class Cat(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)
        
    def make_sound(self):
        print('meow')

d1 = Dog("Buddy", "Canine")
d1.make_sound()  # Woof!

c1 = Cat("Kitty", "Feline")
c1.make_sound() 
        