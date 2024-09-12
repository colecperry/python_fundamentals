# Define a sample list
sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Print the original list
print("Original list:", sample_list)

# Slice from the start to a specific position
print("Slice from start and stop before index 5 (exclusive):", sample_list[:5])

# Slice from a specific position to the end
print("Slice from index 5 to end:", sample_list[5:])

# Slice between two specific indices
print("Slice from index 2 to 7 (exclusive):", sample_list[2:7])

# Slice with a step
print("Slice entire list with step 2:", sample_list[::2])

# Slice with negative step (reversing the list)
print("Slice entire list with step -1 (reversed):", sample_list[::-1])

# Slice a subset with a step
print("Slice from index 1 to 8 (exclusive) with step 2:", sample_list[1:8:2])

# Slice using negative indices
print("Slice from index -7 to -2 (exclusive):", sample_list[-7:-2])

# Slice with negative step within a range
print("Slice from index 8 to 2 (inclusive) with step -2:", sample_list[8:1:-2])

# Slice the entire list
print("Slice the entire list:", sample_list[:])

# Slice with start and end omitted (same as slicing the entire list)
print("Slice the entire list with omitted start and end:", sample_list[::])

# Slice with only start specified
print("Slice from index 3 to end:", sample_list[3:])

# Slice with only end specified
print("Slice from start to index 6 (exclusive):", sample_list[:6])

# Complex slice example
print("Complex slice: Start at 1, end at -1, step 2:", sample_list[1:-1:2])
