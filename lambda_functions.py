# Lambda functions in Python, also known as anonymous functions, are small, single-expression functions that are defined using the lambda keyword. They are used primarily for short-term use where defining a full function would be overkill.

# Ex. 1 - Adding to a value
new_dozen = lambda n: n + 12

print(new_dozen(0)) # When we invoke new_dozen(), our lambda function will add 12 to the total
print(new_dozen(5))

def myfunc(x):
    return lambda n: n + x

new_century = myfunc(100)
print(new_century(2000))

# Ex. 2 - Sorting
points = [(1, 2), (4, 1), (5, -1), (2, 3)]
points.sort(key=lambda point:point[1])
print(points)

l = [['red', 'truck'], ['blue', 'car'], ['red', 'sedan']]
l2 = sorted(l, key=lambda v: v[1], reverse=True) # Sorted accepts the iterable you want to sort, the key, and reverse(optional)
print(l2)

# Ex. 3 - Filtering
numbers = [1,2,3,4,5,6,7,8,9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # Filter accepts two arguments, a function and an iterable
print(even_numbers)

# Ex. 4 - Mapping
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

# Ex. 5 - Inline functions
add = lambda x, y: x + y
print(add(3, 5))

# Ex. 6 - Return lambdas as new, unique functions
def myfunc(x):
  return lambda a, b : (a + b) * x

sum_times_2 = myfunc(2)

print(sum_times_2(10, 20))