# Object Inheritance - a class can inherit all the attributes and methods from another class, called the superclass

# Class Introspection - when multiple classes define the same method. For example, in the go method, the interpreter will first look in the class to which the instance of car that we are calling the method on belongs. If it finds a go() method there, it will execute that method. If it doesn't find such a method there, it will move on to look in the parent class that this class inherits from.

class Vehicle:
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        return "filling up!"

# We use Vehicle as an argument for the Car class to note that Car inherits from Vehicle. 
class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    
# __bases__ attribute - asks a class what class they inherit from
print("Car class inherits from: ", Car.__bases__)


# Initalize a Vehicle
sedan = Vehicle("18 inch", 0)
print(sedan.go())

# Initialize a Car - when you create an instance of a subclass, you have to pass in the same parameters required by the superclass's __init__ function
acura = Car("17 inch", 4)
print("wheel size: ", acura.wheel_size)
print("wheel number: ", acura.wheel_number)
print(acura.go())

# Super
# User is the parent class
class User:
    def __init__(self, name):
        print("User.__init__ called.")
        self.name = name

    def log_in(self):
        print("User.log_in() called.")
        self.logged_in = True

class Student(User):
    def __init__(self, name, grade):
        print("Student.__init__ called.")
        super().__init__(name) # When we initialize a student, we also initialize a student with a name
        self.grade = grade

    def log_in(self):
        print("Student.log_in() called.")
        super().log_in() # We use super to call the log_in() method and inherit and functionality from the parent class
        self.in_class = True

oneil = Student("oneil", 100)
oneil.log_in()
print(oneil.logged_in)

