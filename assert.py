# assert B,S: B is a boolean expression, S is a string. If B is not true, then string S is printed and an exception is raised. Otherwise, nothing is done.
def sqrt(x):
    assert x>0, 'The sqrt function requires a positive argument.'
    L = float(x)
    L = (L+x/L)/2
    L = (L+x/L)/2
    L = (L+x/L)/2
    L = (L+x/L)/2
    assert abs(L*L-x)<=.001,'Inaccurate Square Root'
    return L

print(sqrt(9), "is the square root of 9\n")
print(sqrt(-12), "\n")