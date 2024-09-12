# Sets:
    # Use { and }
    # Can store all types of data
    # Are unindexed
    # Are mutable or not mutable based on if they are frozen or not
    # Items can not be repeated
    # Items can not be changed or replaced

# Importing the math module for square root calculations
from math import sqrt

# Creating a set
s = {1, 2, 3, 2, 1}
print("set:", s) # notice how duplicates are removed

s2 = "the big red cat ate the fat rat"
print(set(s2))
print("\n")

# Methods available to set
print("Methods available to set:")

# add() method - add an element to the set
s.add(4)
print("add():", s)

# clear() method - remove all elements from the set
s.clear()
print("clear():", s)
s = {1, 2, 3}  # Re-adding elements for further demonstration

# copy() method - copy all elements from the set
s_copy = s.copy()
print("copy():", s_copy)

# difference() method - returns elements that are part of either of the two sets but not both
s_diff = s.difference({2, 3})
print("difference():", s_diff)
    # OR
print(s - {2,3})

    # Dynamically modify your sets
set_1 = {1,2,3}
set_2 = {3,4,5}

# set_1 = set_1 & set_2 
set_1 &= set_2
print("set_1 and set_2 = set_1: ", set_1)

# difference_update() method
s.difference_update({2, 3})
print("difference_update():", s)
s = {1, 2, 3}  # Re-adding elements for further demonstration

# discard() method - remove a specific element from the set
s.discard(2)
print("discard():", s)

s = {1, 2, 3}  # Re-adding elements for further demonstration

# intersection() method - returns a new set containing only the elements that are common between the specified sets
s_inter = s.intersection({2, 3, 4})
print("intersection():", s_inter)
    # OR
print(s & {2,3,4})

# intersection_update() method
s.intersection_update({2, 3, 4})
print("intersection_update():", s)
s = {1, 2, 3}  # Re-adding elements for further demonstration

# isdisjoint() method - returns True if the two sets have no elements in common
is_disjoint = s.isdisjoint({4, 5})
print("isdisjoint():", is_disjoint)

# issubset() method - returns True if the set "s" is a subset of the set passed in as the argument
is_subset = s.issubset({1, 2, 3, 4})
print("issubset():", is_subset)

# issuperset() method - returns true if "s" contains all the elements from the set passed in as the argument
is_superset = s.issuperset({1, 2})
print("issuperset():", is_superset)

# List comprehensions
sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
unique_consonants = {c.lower() for c in sentence if c not in "aeiou ,."}
print("unique consonants: ", unique_consonants)

# pop() method - removes the first item from the set
popped_element = s.pop()
print("pop():", popped_element, "set after pop():", s)

s = {1, 2, 3}  # Re-adding elements for further demonstration

# remove() method - remove the element passed in
s.remove(3)
print("remove():", s)

s = {1, 2, 3}  # Re-adding elements for further demonstration

# symmetric_difference() method - returns a new set containing elements that are in either of the sets but not both
s_sym_diff = s.symmetric_difference({2, 3, 4})
print("symmetric_difference():", s_sym_diff)

# symmetric_difference_update() method
s.symmetric_difference_update({2, 3, 4})
print("symmetric_difference_update():", s)
s = {1, 2, 3}  # Re-adding elements for further demonstration

# union() method - returns a new set that contains all unique elements from all the sets involved
s_union = s.union({3, 4, 5})
print("union():", s_union)

# update() method - updates the set "s" by adding elements from another set
s.update({3, 4, 5})
print("update():", s)

# Frozen Sets (Immutable Sets)
print("Frozen Sets (Immutable Sets)")

# Creating a frozenset
fs = frozenset([1, 2, 3, 2, 1])
# Notice the set automatically removes duplicate elements 
print("frozenset:", fs) 

# Methods available to frozenset
print("Methods available to frozenset:")

# copy() method
fs_copy = fs.copy()
print("copy():", fs_copy)

# difference() method - returns a new set containing all the elements in the original set and not the other set passed in
fs_diff = fs.difference(frozenset([2, 3]))
print("difference():", fs_diff)

# intersection() method - returns a new set containing only the elements that are common between the specified sets
fs_inter = fs.intersection(frozenset([2, 3, 4]))
print("intersection():", fs_inter)

# isdisjoint() method - returns True if the two sets have no elements in common
is_disjoint = fs.isdisjoint(frozenset([4, 5]))
print("isdisjoint():", is_disjoint)

# issubset() method - returns True if the set "fs" is a subset of the set passed in as the argument
is_subset = fs.issubset(frozenset([1, 2, 3, 4]))
print("issubset():", is_subset)

# issuperset() method - returns true if "fs" contains all the elements from the set passed in as the argument
is_superset = fs.issuperset(frozenset([1, 2]))
print("issuperset():", is_superset)

# symmetric_difference() method - returns a new set containing elements that are in either of the sets but not both
fs_sym_diff = fs.symmetric_difference(frozenset([2, 3, 4]))
print("symmetric_difference():", fs_sym_diff)

# union() method - returns a new set that contains all unique elements from all the sets involved
fs_union = fs.union(frozenset([3, 4, 5]))
print("union():", fs_union)

# Sets (Mutable Sets)
print("\nSets (Mutable Sets)")


