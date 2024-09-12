# ShowSelect.py
""" Uses Selection Sort to illustrate how functions
with list parameters work."""

from random import randint as randi
from random import seed

def Select(a,i):
    """ Swaps the smallest value in a[i:] with a[i]
    
    PreC: a is a list of integers and i is an in that
    satifies 0<=i<len(a)
    """
    n = len(a) # "n" is the length of the list
    imin = i # Create variable "imin" to point at the lower index you are going to replace, which is determined by the selctionSort fn
    min_x = a[i] # Create variable "min_x" to point at the lower value you are going to replace
    for k in range(i+1,n): # Loop through the rest of the list to find the smallest value
        if a[k] < min_x: # If the value you are iterating on is less than the min value
            imin=k # If yes, point "imin" at the second index k
            min_x = a[k] # Replace "min_x" value with the smaller value you found at index k
            print("min_x:", min_x)
    # Swap x[i] with the minimum value
    temp = a[i] # Point temp variable at the lower index you are going to replace
    a[i] = a[imin] # Swap the value at the lower index 
    a[imin] = temp

def SelectionSort(a):
    """ Permutes the values in list a so that they
    range from smallest to largest.
    
    PreC: a is a nonempty list of numbers.
    """
    n = len(a) # n equals the length of the list
    for k in range(n): # Loop through the list "n" times
        Select(a,k) # And run Select with the list and the loop variable 0 through n passed in
        # a[0:(k+1)] is sorted
        print (a)
    
    
def randiList(L,R,n):
    """ Returns a length-n list of random integers
    selected from the interval [L,R].
    
    PreC: L, R, and n are ints with n>0 and L<R.
    """
    seed(0)
    t = []
    for k in range(n): # Loop "n" times 
        r = randi(L,R) # Generate a random number between 1 and 100
        t.append(r) # and append to the list
    return t
    
    
if __name__ == '__main__':
    # Create a list of 10 random numbers between 1 and 100
    a = randiList(1,100,10)
    print (a)
    SelectionSort(a)