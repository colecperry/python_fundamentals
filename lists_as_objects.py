from copy import copy, deepcopy

# In this code, x and y point to the same object in memory, so when you modify x, you are also modifying y
x = [10,20,30,40]
y = x
for k in range(4):
    print ("x is", x )
    print ("y is", y )
    print ("...." )
    x[k] = y[3-k]
print (x)
print('\n')


