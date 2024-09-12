# Linear search with for loop
def LinSearch(x,a):
    """ Returns an int k with the property that a[k]==x is True.
    If no such k exists, then k==-1.
    PreC: a is a nonempty list of ints and x is an int.
    """
    for k in range(len(a)):
        if x == a[k]:
            return k
    return -1
    
print(LinSearch(23, [86,73,43,35,23,45,42,62]))

# Linear search with while loop
def LinSearchWhile(x,a):
    k = 0
    while k<len(a) and a[k] != x: # Continue loop until k is greater than the length of the list or the current value in the list is equal to x
        k+=1
        
    if k == len(a):
        return -1
    else:
        return k

print(LinSearch(43, [86,73,43,35,23,45,42,62]))