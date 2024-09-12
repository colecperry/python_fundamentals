from math import sqrt
# def sumRecList(lis):
#     if len(lis) == 0:
#         return 0
#     else:
#         smaller = sumRecList(lis[1:])
#         print(smaller)
#         new_sum = sum(smaller)
#         total = new_sum + total

# sumRecList([1,[3,4],[5,6]])

# # Call block sumRecList([1,[3,4],[5,6]]) is called. Length of the list is not 1 so enter else block. Call sumRecList([3,4],[5,6]) and smaller does not store anything yet.
# # Call block sumRecList([3,4],[5,6]) is called. Length of the list is not 1 so enter else block. Call sumRecList([5,6]) and base case is hit and returns [5,6] to smaller in sumRecList([3,4],[5,6]) call block. Add numbers together and add to total.

# How attributes update
class Point1:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.d = sqrt(x**2 + y**2)

# Notice here that d is not updated, you are only modifying the x attribute
P = Point1(3,4)
P.x = 0
print (P.d)

# Notice here you are updating d after modifying x
P.d = sqrt(P.x**2 + P.y**2)
print(P.d)
