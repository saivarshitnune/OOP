# 🔷 1. Multiple Inheritance
# ✅ What is it?
# In multiple inheritance, a class (child) inherits from more than one parent class. 
# It allows the child class to use features (methods/attributes) of all its parent classes.


# class Parent1:
#     pass

# class Parent2:
#     pass

# class Child(Parent1, Parent2):
#     pass



class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        print(f"Employee Name: {self.name}")

class Programmer:
    def __init__(self, language):
        self.language = language

    def get_skills(self):
        print(f"Programming Language: {self.language}")

class Developer(Employee, Programmer):
    def __init__(self, name, language):
        Employee.__init__(self, name)
        Programmer.__init__(self, language)

    def show_profile(self):
        self.get_details()
        self.get_skills()

d1 = Developer("Varshith", "Python")
d1.show_profile()

