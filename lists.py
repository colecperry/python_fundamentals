# Lists:
    # Can store all types of data
    # Are indexed
    # Are mutable
    # Items can be repeated
    # Items can be changed or replaced

# Example list
x = [3, 5, -1, 0, 3.14]
z = ['This is a long sentence', 'Word', 'z']

# Assign variable to an element of a list
a = x[0]
print("Value at index 0:", a)
print("\n")

# List slicing
y = x[:2]
print("First two elements:", y)
print("\n")

# Lists are mutable - change the element of a list by reassigning it
x[0] = 1
print("After changing first element:", x)
x[1:3] = [100, 200]
print("After changing elements 1 and 2:", x)
print("\n")

# List methods - append, extend, insert, sort
# Append - add an element to the end of a list - RETURNS NONE
x.append(1000)
print("After appending 1000:", x)
print("\n")

# Extend - when you want to "glue" one list onto the end of another list. Returns none.
t = [2000, 3000]
x.extend(t)
# Notice that the extend method modifies the original list in place and returns none
print("After extending with [2000, 3000]:", x)
print("\n")

# Insert an item into the list. Items get bumped to the right. Returns none
x.insert(0, 2)
print("After inserting 2 at index 0:", x)
print("\n")

# Sort - sort the list in alphabetical or numerical order, or in reverse. Returns none
x.sort()
print("After sorting in ascending order:", x)

x.sort(reverse=True)
print("After sorting in descending order:", x)

z.sort(key=len)
print("Sort by key length: ", z)
print("\n")

# Pop - Removes an element at a certain index and returns that node, if no index passed it removes the last item
i = 2
m = x.pop(i)
print("Popped element at index 2:", m)
print("list after pop: ", x)
print("\n")

# del - removes elements from a list specified by an index or range 
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
del(my_list[0])
print("my list with deleted 0th index: ", my_list)

del(my_list[0:3])
print("my list with three more items deleted: ", my_list)

print("\n")

# remove - removes the element passed in as the argument, but searches with value instead of index
my_list_2 = [0, 100, 'bob', 'cat']
my_list_2.remove('bob')
print("List after remove: ", my_list_2)

# Count - counts the number of items in a list that have a specific value, or 0 if none
c = x.count(0)
print("Number of occurrences of 0:", c)

d = x.count(99)
print("Number of occurrences of 99:", d)
print("\n")

# Sum - sums all the items in the list
s = sum(x)
print("Sum of elements in the list:", s)
print("\n")

# Lists of strings:
s2 = ['cat', 'dog', 'mouse']

# Get subscript from the string
c = s2[2][1:3]
print("Substring of 'mouse':", c)
print("\n")

t = s2[1]
d = t[1:]
print("Substring of 'dog':", d)
print("\n")

# Compare two lists - must have same values and length, but they are not the same object
a1 = [1, 2, 3, 4]
a2 = [1, 2, 3, 4]
a3 = [1.0, 2.0, 3, 4.0]
print("Comparison of a1 and a2:", a1 == a2)
print("Comparison of a2 and a3:", a2 == a3)
print("Identity comparison of a1 and a2:", a1 is a2)
print("\n")

# Make a copy of a list
a4 = list(a1)
print("Copy of list a1:", a4)
print("\n")

# print loop of list
for k in range(len(a1)):
    print(a1[k])
    print("\n")

# Sort a list of objects by a key
objects = [{'name': 'John', 'age': 30},
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 35}]

# Define a custom function to extract the key (e.g., 'age') from each object
def get_age(obj):
    return obj['age']

# Sort the list of objects by the 'age' key using the custom function.
# In python, sorted(), min(), and max() can accept a key function as an argument
# The sorted function iterates over each object in the objects list, and applies the get_age function to extract the value associated with the 'age' key
sorted_objects = sorted(objects, key=get_age)
print(sorted_objects)
print("\n")


