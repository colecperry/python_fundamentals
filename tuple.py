# Tuples are identical to lists, except:
    # They are created with open and close parentheses
    # Tuples are immutable

# Creating a tuple
new_tuple = tuple()

original_tuple = (1, 2, 3)
print("original tuple:", original_tuple)

# How to add data to a tuple
# 1. Concatenation
new_element = 4
# When adding to a tuple in python you have to include a comma inside the parentheses to ensure the item being added is regonized as a tuple
new_tuple = original_tuple + (new_element,) 
print("new tuple with new element 4:", new_tuple)

new_elements = (4, 5, 6)
new_tuple_2 = original_tuple + new_elements

print("new tuple with new elements 4, 5, and 6:", new_tuple_2)

# 2. Using a list conversion - convert tuple to list and then back to a tuple
temp_list = list(original_tuple)

# Add new elements
temp_list.append(4)
temp_list.extend([5,6])

# Convert back to tuple 
new_tuple_3 = tuple(temp_list)

print("new tuple after adding elements using list conversion:", new_tuple_3)
print("\n")

# Other methods that work on tuples

# Count
x = new_tuple_3.count((1))
print("count:", x)
print("\n")

# Index Search
# index(value, start, stop) - returns index of the first occurrence of that specified value. The start and stop parameters are optional and specify a range to search
a = new_tuple_3.index(3)
print("find first occurrence of 3:", a)
b = new_tuple_3.index(5,2,5)
print("find first occurrence of 5 between indexes 2 and 5:", b)
print("\n")

# Find Index
index_0 = new_tuple_3[0]
print("index 0: ", index_0)
print("\n")

# Slicing
slice_1 = new_tuple_3[1:3]
print("sliced tupled: ", slice_1)
print("\n")

# In - check for membership
tuple_4 = (2,4,6,8)
print(2 in tuple_4)
print("\n")

# Sort by key
tuple_5 = [('John', 2), ('Steve', 1), ('Joe', 3)]

def sort_tuple(tuple_value):
    # Return the key we want to sort by
    return tuple_value[1]

tuple_5.sort(key = sort_tuple)

print("Sorted tuple by integer: ", tuple_5)




