# Abstraction means hiding the internal details and showing only the essential features to the user.

# In Python, abstraction is achieved using abstract classes and abstract methods.

# 🔧 Why Use Abstraction?
# To define a common interface for all child classes

# To ensure certain methods must be implemented in subclasses

# To make code more organized, reusable, and secure

from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass

# Subclass 1
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

# Subclass 2
class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

# Using the classes
p1 = CreditCardPayment()
p1.pay(500)

p2 = PayPalPayment()
p2.pay(700)


# output

# Paid 500 using Credit Card.
# Paid 700 using PayPal.




# ✅ Key Points:
# Payment is an abstract class. It cannot be instantiated directly.

# pay() is an abstract method: every subclass must implement it.

# You define a blueprint (interface) in the abstract class, and write logic in child classes.