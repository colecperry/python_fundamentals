def recursiveAddCards(cards):
    if cards == []:
        return 0
    else:
        smallerProblem = cards[1:]
        smallerResult = recursiveAddCards(smallerProblem)
        return cards[0] + smallerResult
    

recursiveAddCards([5, 2, 7, 3])

# How the code works
# Call block recursiveAddCards([5, 2, 7, 3])
    # recursiveAddCards([5, 2, 7, 3]) is called
    # Since cards is not empty, enter else statement
    # smallerProblem stores slices off the first card and stores ([2,7,3])
    # recursiveAddCards([2,7,3]) is called, but code waits to store a value because it has not returned anything

# Call block recursiveAddCards([2, 7, 3])
    # recursiveAddCards([2, 7, 3]) is called
    # Since cards is not empty, enter else statement
    # smallerProblem slices off the first card and stores ([7,3])
    # recursiveAddCards([7,3]) is called, but code waits to store a value because it has not returned anything

# Call block recursiveAddCards([7, 3])
    # recursiveAddCards([7, 3]) is called
    # Since cards is not empty, enter else statement
    # smallerProblem slices off the first card and stores ([3])
    # recursiveAddCards([3]) is called, but code waits to store a value because it has not returned anything

# Call block recursiveAddCards([3])
    # recursiveAddCards([3]) is called
    # Since cards is not empty, enter else statement
    # smallerProblem slices off the first card and stores ([])
    # recursiveAddCards([]) is called, and hits the base case and returns 0

# BACK UP THE STACK
    # recursiveAddCards([3]) is waiting for the the smallerResult variable (recursiveAddCards([0])), which returned 0 when the base case is hit. Now we continue to the return statement cards[0] + smallerResult, and returns 3 + 0 = 3 for recursiveAddCards([3]). 

    # recursiveAddCards([7,3]) is waiting for the smallerResult variable (recursiveAddCards([3])), which returned 3. Now we continue to the return statement cards[0] + smallerResult = 7 + 3 = 10 for recursiveAddCards([7,3]) 

    # recursiveAddCards([2,7,3]) is waiting for the smallerResult variable (recursiveAddCards([7,3])), which returned 10. Now we continue to the return statement cards[0] + smallerResult = 2 + 10 = 12 for recursiveAddCards([2,7,3])

    # recursiveAddCards([5,2,7,3]) is waiting for the smallerResult variable (recursiveAddCards([2,7,3])), which returned 12. Now we continue to the return statement cards[0] + smallerResuly = 5 + 12 = 17 for recursiveAddCards([5,2,7,3])