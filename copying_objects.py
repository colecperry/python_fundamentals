from copy import copy, deepcopy

class MyColor:
    '''Attributes:
        rgb: lenth-3 float list
        name: str
    '''
    def __init__(self, rgb, name):
        self.rgb = rgb
        self.name = name
    
# Create an instance of the MyColor class and create a copy
A = MyColor([1,0,0], 'red')
B = copy(A)

print("A before any changes", A.rgb)

# Change the A instance's rgb
A.rgb[1] = 1
print("A after changing the second value", A.rgb)
print("B after A changed the second value", B.rgb) # <- Notice how B.rgb also changes

# Deepcopy
E = MyColor([2,2,2], "blue")
C = deepcopy(E)

print("E before any changes", E.rgb)

E.rgb[1] = 1
print("E after changing the second value", E.rgb)
print("C after E changing the second value", C.rgb) # <- Does not change