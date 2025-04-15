# 🧩 What is Polymorphism?
# Polymorphism simply means:

# "Same function name or method behaves differently based on the object calling it."

# 📌 In Greek, poly = many, morph = forms.
# So, polymorphism = many forms of the same method or operation.


# ✅ Types of Polymorphism in Python:

# Compile-Time Polymorphism (Method Overloading – doesn't support in Python)
# It can be simulated using default arguments or variable-length arguments.
# Example: Method Overloading

class Calculator:
    def add(self, *args):  # accepts multiple arguments
        return sum(args)

calc = Calculator()

print(calc.add(1, 2))           # 3
print(calc.add(5, 10, 15))      # 30
print(calc.add(10))             # 10

# ✅ What is *args?
# *args means "take any number of arguments and store them as a tuple".

# Then we just do sum(args).

# This is great when we don’t know how many numbers the user will give.


# Run-Time Polymorphism (Method Overriding – commonly used)
class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Polymorphism in action
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.make_sound()
# Output:
# Woof!
# Meow!
# Some generic sound
