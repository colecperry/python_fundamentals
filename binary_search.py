# Assume the list is sorted from little to big
# The idea is repeatedly halving the size of the "search space"
def BinSearch(x,a):
    """ Returns an int k with the property that
    a[k]==x is True. If no such k exists, then
    -1 is returned.
    
    PreC: a is a nonempty list of ints that is sorted from smallest
    to largest. x is an int.
    """
    if x<a[0] or x>a[-1]: # Check if x is outside the interval [a[0],a[-1]]
        return -1
    L = 0 # Initialize L and R
    R = len(a)-1
    while R-L > 1: # Continue loop until the difference between L and R is 1
        assert a[L]<=x<=a[R], 'x is not in interval [a[L],a[R]]'
        mid = int((L+R)/2) # Calculate the midpoint
        if x < a[mid]: # Update L and R depending on the positioning of x
            R = mid
        else:
            L = mid
    assert a[L]<=x<=a[L+1], 'R does not equal L+1'
    if a[L]==x: # Once you break out of the loop, L and R should be apart by 1, so check both
        return L
    elif a[L+1]==x:
        return L+1
    else:
        return -1

print(BinSearch(6, [0,2,4,6,8,10,12,14,16,18]))