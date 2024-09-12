from copy import copy
from math import sqrt

# Classes are used to "package" related data

class Point(object):
    """
    Attributes:
    x: float, the x-coordinate of a point
    y: float, the y-coordinate of a point
    """
    # The special function, called the constructor, does the packaging
    # "self" is always the first argument for any method defined in a class
    # you can set a defult value for y if none is given
    def __init__(self,x,y = 0):
        self.x = x
        self.y = y

# Calling the constructor creates an object, or an instance
Q = Point(3,4)
print("This is an instance: ", Q)

# Accessing attributes 
print("Instance Q's x attribute: ", Q.x)
print("Instance Q's y attribute: ", Q.y)

# Change an attribute
Q.y = Q.y + 5
print("Changed y attribute: ", Q.y)

# Create a copy of an instance - does not change original if you update the copy
P = Point(Q.x, Q.y)
# or... (must import copy)
P1 = copy(Q)
print("copied instance: ", P1.x, P1.y)
print("original instance: ", Q.x, Q.y)
P1.x = 5
print("copied and modified instance: ", P1.x, P1.y)
print("Does the original Q change? ", Q.x, Q.y) # no
print('\n')

# This only creates an alias - if you change attributes of the alias, the original changes too
V = Point(1,2)
Y = V
print("V: ", V.x, V.y)
print("Y: ", Y.x, Y.y)

# Changing an attribute of an alias
Y.x = 0
print("Y.x after changing: ", Y.x)
print("V.x after changing Y.x: ", V.x)

# What if we create another instance?
V = Point(0,0)
print("V after new instance: ", V.x, V.y)
print("Y after creating a new V instance: ", Y.x, Y.y) # Y still points to first instance
print('\n')

# How attributes update
class Point1:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.d = sqrt(x**2 + y**2)

# Notice here that d is not updated, you are only modifying the x attribute
# The attribute d is only calculated once during the init method, when you update an attribute it does not automatically trigger a recalculation of 'd'
P = Point1(3,4)
P.x = 0
print ("P.d after changing x:", P.d)

# Notice here you are updating d after modifying x
P.d = sqrt(P.x**2 + P.y**2)
print("P.d after updating x:", P.d)
print("\n")

# Instance attributes - all of an objects methods can be accessed with the instance's __dir__() method

print("__dir__():", P.__dir__())

# Class Attributes - species is set outside the init method, so every human has the same species attribute
class Human:
    species = "Homo sapiens"
    def __init__(self, name):
        self.name = name

guido = Human("Guido")

# getattr(), setattr(), hasattr(), and delattr() - similar to dot notation
print("\nClass Attributes:")
print("getattr():", getattr(guido, "name"))

setattr(guido, "nationality", "Dutch")
print("setattr():", guido.nationality)

print("hasattr():", hasattr(guido, "nationality"))

delattr(guido, "nationality")
print("hasattr():", hasattr(guido, "nationality"))
print("\n")

# Private members - a private member of a class is an attribute or method that is intended to be accessed only within the class itself. Private members are not strictly enforced by Python, but by convention, a member is considered private if its name starts with a double underscore (__). Private members cannot be accessed directly via dot notation but can be accessed via functions (usually getter and setter functions)

class MyClass:
    def __init__(self, public_value, private_value):
        self.public_value = public_value  # Public attribute
        self.__private_value = private_value  # Private attribute

    def get_private_value(self):
        return self.__private_value

    def set_private_value(self, new_value):
        self.__private_value = new_value

    def __private_method(self):
        print("This is a private method.")

    def call_private_method(self):
        self.__private_method()


# Creating an instance of MyClass
obj = MyClass("public", "private")

# Accessing the public attribute
print("Public value:", obj.public_value)

# Trying to access the private attribute directly (will raise an AttributeError)
try:
    print("Private value (direct access):", obj.__private_value)
except AttributeError as e:
    print("Error:", e)

# Accessing the private attribute via a public method
print("Private value (via method):", obj.get_private_value())

# Setting the private attribute via a public method
obj.set_private_value("new_private")
print("Updated private value (via method):", obj.get_private_value())

# Trying to call the private method directly (will raise an AttributeError) - private methods cannot be accessed from outside the class
try:
    obj.__private_method()
except AttributeError as e:
    print("Error:", e)

# Calling the private method via a public method - can use another function that is not private to call the private method - LOL
obj.call_private_method()

# Demonstrating name mangling (not recommended for regular use)
print("Accessing private value via name mangling:", obj._MyClass__private_value)


