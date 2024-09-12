import math

class Point:
    """ Attributes:
    x the x-coordinate [float]
    y the y-coordinate [float]
    """
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def Dist(self,other):
        """ Returns a float that is the distance from self to other.
        Precondition: other is a Point """

        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
    
    def FarthestPt(L, idx, P):
        """ Returns an integer j with the property that the distance from
        L[j] to P is maximum among all the ***unvisited*** points.

        If idx[i] = 1, then we say that L[i] has been visited. If idx[i] = 0, then
        we say that L[i] is unvisited.

        Preconditions: L is a list of references to Point objects, P is a
        reference to a point object, and idx is a list of ints that are either
        zero or 1. The lists idx and L have the same length and idx has at
        least one zero entry. """
        max_distance = 0
        furthest_index = -1 # Initalize the furthest index since we need to return an index
        for i in range(len(idx)): # Loop through the "idx" list which tells us visited/unvisited points
            if idx[i] == 0: # If the index is 0, that means the point is unvisited
                distance = L[i].Dist(P) # Call the distance method on the point P and the proper indexed instance in the list L
                if distance > max_distance: # Update max distance if it is greater
                    max_distance = distance
                    farthest_index = i # Update the fathest index if the distance is further
        return farthest_index
                

L = [Point(1,5), Point(2,4), Point(5,10)]
P = Point(1,1)
idx = [0,1,0]
print(Point.FarthestPt(L, idx, P))  # Output should be 2

