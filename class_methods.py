from math import sqrt
import random

class Point(object):
    """
    Attributes:
    x: float, the x-coordinate of a point
    y: float, the y-coordinate of a point
    """
    # The special function, called the constructor, does the packaging
    # "self" is always the first argument for any method defined in a class
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    # This is a class method, the first argument is always "self"
    def Dist(self, other):
        """ Returns distance from self to other.
        PreC: other is a point
        """
        dx = self.x - other.x
        dy = self.y - other.y
        d = sqrt(dx**2+dy**2)
        return d

    
P = Point(3,4)
Q = Point(6,8)

# Note - P is passed in as the first arg on Dist, and Q is passed in as the second arg
D = P.Dist(Q)
print(D)
print("\n")

# List of Objects
A = Point(1,2)
B = Point(3,4)
C = Point(5,6)
L = [A,B,C]
print("Print the list of point class objects", L)
print("\n")
first_obj = L[0]
print("Print the first object in the list: ", first_obj.x, first_obj.y)
print("\n")
first_obj.x = 2
print("First object after changing x: ", first_obj.x, first_obj.y)
print("\n")
L[0] = Point(0,0)
print("First object after changing instance in list: ", L[0].x, L[0].y)
print("\n")

class Album:
    album_count = 0
    GENRES = ["Hip-Hop", "Pop", "Jazz"] # This is a class constant -> data does not change

    def __init__(self, date):
        Album.album_count += 1 # Use dot notation to access the album_count variable outside the init fcn
        self.release_date = date

    @classmethod # class method provides a convenient way to modify class-lvel data that belongs to the class rather than the instances
    def increase_album_count(cls, increment=1):
        cls.album_count += increment

Album("Jan 1, 1490")
Album("Jan 1, 1500")
Album("Jan 1, 1788")
print("Album count after init:", Album.album_count)

Album.increase_album_count(2)
print("Album count after increase:", Album.album_count)



