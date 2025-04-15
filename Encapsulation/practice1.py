
#Student Grade System
# Create a Student class with private attribute grade. Add:

# A method to set the grade (0 to 100 only)

# A method to get the grade

class StudentGradeSystem:
    
    def __init__(self):
        self.__grade = 0
    
    def set_grade(self,data):
        if 0<data<100:
            self.__grade=data
        else:
            print('invalid input')
    def get_grade(self):
        print(self.__grade)

s1 = StudentGradeSystem()
s1.set_grade(95)
s1.get_grade()
            


#Password Locker
# Create a class Locker with a private message and password.

# Only show the message if the correct password is given

class PasswordLocker:
    def __init__(self,message,password):
        self.__message = message
        self.__password = password
    
    def get_message(self,data):
        if self.__password == data:
            print('message -' , self.__message)
        else:
            print('Incorrect password')

p1=PasswordLocker('how are you darling',143)
p1.get_message(143)
    



###Book Borrowing System
# Library Book Borrow System
# Build a Book class:

# Private attribute for availability (True/False)

# Method to borrow a book (only if available)

# Method to return the book


class Book:

    def __init__(self, title):
        self.__title = title
        self.__available = True  # book is available initially

    def borrow_book(self):
        if self.__available:
            self.__available = False
            print(f"You have borrowed '{self.__title}'.")
        else:
            print(f"Sorry, '{self.__title}' is already borrowed.")

    def return_book(self):
        if not self.__available:
            self.__available = True
            print(f"You have returned '{self.__title}'.")
        else:
            print(f"'{self.__title}' was not borrowed.")

    def check_availability(self):
        status = "Available" if self.__available else "Not Available"
        print(f"'{self.__title}' status: {status}")
