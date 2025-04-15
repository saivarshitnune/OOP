# In Multilevel Inheritance, a class inherits from a class which in turn inherits from another class.

#Grandparent → Parent → Child


class Animal:
    def __init__(self):
        print("I am an Animal")

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("I am a Mammal")

class Dog(Mammal):
    def __init__(self):
        super().__init__()
        print("I am a Dog")

d = Dog()




# 1. College Member Hierarchy
# Create a class Person with attributes name and age.
# Create a class Student that inherits from Person and adds student_id.
# Then create a class GraduateStudent that inherits from Student and adds thesis_title.

# Write a method in GraduateStudent to display all the info.




class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id

class GraduateStudent(Student):
    def __init__(self,name,age,student_id,thesis_title):
        super().__init__(name,age,student_id)
        self.thesis_title = thesis_title
        
    def display(self):
        print(f'Name - {self.name}')
        print(f'Age - {self.age}')
        print(f'student-id - {self.student_id}')
        print(f'thesis-tile - {self.thesis_title}')

g1 = GraduateStudent('sreekar',28,18908,'Deep nueral networks')
g1.display()


# GraduateStudent.__init__('sreekar', 28, 18908, 'Deep neural networks')
#     ↓
#     Calls super().__init__('sreekar', 28, 18908)
#     ↓
# Student.__init__('sreekar', 28, 18908)
#     ↓
#     Calls super().__init__('sreekar', 28)
#     ↓
# Person.__init__('sreekar', 28)
#     ↓
#     Sets self.name = 'sreekar'
#          self.age = 28
#     ↑
# Returns to Student.__init__()
#     Sets self.student_id = 18908
#     ↑
# Returns to GraduateStudent.__init__()
#     Sets self.thesis_title = 'Deep neural networks'
