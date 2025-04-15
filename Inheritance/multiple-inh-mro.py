# MRO (Method Resolution Order) determines the order in which classes are searched when executing a method or looking up an attribute in inheritance hierarchy,
# especially when multiple inheritance is involved.

# Python uses the C3 Linearization algorithm to compute MRO.


# ✅ Why MRO is Important?
# When a method or attribute is present in multiple parent classes, 
# MRO ensures a consistent and predictable order of which class Python should refer to first.


#C3 Linearization algorithm
# MRO tries to:

# Preserve local precedence order (left to right).

# Ensure that a class always appears before its parents.

# Avoid duplication and maintain consistency.


class Printer:
    def connect(self):
        print("Connecting to Printer")

class Scanner:
    def connect(self):
        print("Connecting to Scanner")

class MultiFunctionDevice(Printer, Scanner):
    pass

mfd = MultiFunctionDevice()
mfd.connect()

# Output: Connecting to Printer
# The MRO for MultiFunctionDevice is:  [MultiFunctionDevice, Printer, Scanner, object]
# The connect method from Printer is called first because it appears before Scanner in the inheritance order.



class X:
    def greet(self): print("Hello from X")
class Y(X): pass
class Z:
    def greet(self): print("Hello from Z")
class W(Y, Z): pass

w = W()
w.greet()
# Output: Hello from X
# The MRO for W is: [W, Y, X, Z, object]
# The greet method from X is called first because W inherits from Y, which inherits from X.