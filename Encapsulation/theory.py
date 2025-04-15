# 🛡️ What is Encapsulation?
# Encapsulation is the bundling of data (attributes) and methods (functions) that operate on that data within a single unit (class) — and 
# it restricts direct access to some of an object's components.

# Think of it like putting your valuables in a locker. 
# You own the items, but no one can directly access them unless you give permission (like a password or a key). 🔐

# ✅ Goals of Encapsulation:
# Data Hiding: Prevents direct access to class data.

# Control Access: Use methods to read or change data safely.

# Improve Code Security & Integrity.

# 🎯 Syntax in Python:
# Public attributes/methods → can be accessed anywhere.

# Private attributes/methods → prefix with __ (double underscore).

#Without encapsulation-

class Student:
    def __init__(self):
        self.score = 0  # public

    def set_score(self, score):
        if 0 <= score <= 100:
            self.score = score
        else:
            print("Invalid score!")

    def get_score(self):
        return self.score


# Create object
student = Student()

# Set a valid score
student.set_score(90)
print("Score after set_score(90):", student.get_score())  # Expected: 90

# Now directly assign an invalid value
student.score = "banana"
print("Score after student.score = 'banana':", student.get_score())  # Uh-oh! Now it's a string

# Try using this score in a logic that expects a number
if student.get_score() > 50:
    print("Grade: Pass")
else:
    print("Grade: Fail")




# With encapsulation-
class Student:
    def __init__(self):
        self.__score = 0  # private

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            print("Invalid score!")

    def get_score(self):
        return self.__score


student = Student()

student.set_score(90)
print("Score after set_score(90):", student.get_score())  # ✅ 90

# Try to hack it
student.score = "banana"  # Creates a new public attribute, but does NOT affect __score

print("Score after student.score = 'banana':", student.get_score())  # ✅ Still 90

if student.get_score() > 50:
    print("Grade: Pass")  # ✅ Logic works fine
else:
    print("Grade: Fail")
