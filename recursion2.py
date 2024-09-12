#power.py


""" Compares a recursive and nonrecursive implemenatation of
the factorial function.
"""

def power(base, exp):
    """ Returns an int equal to  base**exp
    
    Recursive implementation
    
    PreC: base, exp are nonnegative ints.
    """
    print("base: ", base)
    print("exp: ", exp)
    if exp == 0:
        return 1
    else:
        smaller = power(base, exp-1)
        return base * smaller
    
print("final answer: ", power(2,2))

# How the code works:
#     Call Block power(2,2)
#         power(2, 2) is called.
#         Since exp is not 0, it proceeds to the else block.
#         power(2, 1) is called, but the code waits to store a value for smaller because power(2,1) has not returned       
#         anything yet

#     Call Block power(2,1)
#         Since exp is not 0, it proceeds to the else block.
#         power(2, 0) is called, BASE CASE IS HIT -> Since exp is 0, it returns 1.

#     BACK UP THE STACK
#     Call Block (2,1)
#         Call block (2,1) is waiting for the smaller variable to return the value for              
#         power (2,0). This returned 1 when the base case is hit. Now call block (2,1) stores 1 in 
#         smaller variable for power(2,0), and continues to the return statement base * smaller which equals 2*1 = 2

#     Call Block (2,2)
#         Call block (2,2) is waiting for the smaller variable to return the value for power(2,1), which just returned 2, now we    
#         continue to the final return statement, which is 2 * 2 which returns 4

# In fact, most of the simple recursive functions you write can take the following form:
# def recursiveFunction(problem):
    # if problem == ???: # base case is the smallest value
    # return ____ # something that isn't recursive
# else:
    # smallerProblem = ??? # make the problem smaller
    # smallerResult = recursiveFunction(smallerProblem)
# return ____ # combine with the leftover part