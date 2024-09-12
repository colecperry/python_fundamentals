# Ex.1
for i in range(2):
    for j in range(3):
        print(i,j)
    print('Inner')
print('Outer\n')

# Ex.2 Define the size of the pattern
size = 5

# Upper triangle pattern
print("Upper Triangle Pattern:")
for i in range(size):  # Outer loop for rows
    for j in range(i + 1):  # Inner loop for columns
        print("*", end=" ")  # Print '*' character
    print()  # Move to the next line after printing each row

# Lower triangle pattern
print("\nLower Triangle Pattern:")
for i in range(size):  # Outer loop for rows
    for j in range(size - i):  # Inner loop for columns
        print("*", end=" ")  # Print '*' character
    print()  # Move to the next line after printing each row


# Ex.3 Define the dimensions of the matrix
rows = 3
cols = 3

# Initialize an empty matrix
matrix = []

# Generate the matrix using nested loops
for i in range(rows):  # Outer loop for rows
    row = []  # Initialize an empty list for each row
    for j in range(cols):  # Inner loop for columns
        # Add elements to the row (e.g., using user input or a formula)
        row.append(i * cols + j + 1)
    # Add the completed row to the matrix
    matrix.append(row)

# Print the generated matrix
for row in matrix:  # Outer loop to iterate over rows
    for element in row:  # Inner loop to iterate over elements in each row
        # Print each element with proper formatting
        print(element, end=" ")
    # Print a newline character after each row
    print()
