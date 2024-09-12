# Common errors in Python and when they typically occur

# 1. SyntaxError: Occurs when Python encounters a syntax error while parsing code.
# Example:
# print("Hello, world"  # Missing closing parenthesis
print("Hello, world")

# 2. IndentationError: Occurs when there is an incorrect indentation in the code.
# Example:
# for i in range(5):
# print(i)  # Missing indentation for the print statement
for i in range(5):
    print(i)

# 3. NameError: Occurs when a name (variable, function, etc.) is not found in the current scope.
# Example:
# print(x)  # x is not defined
x = 10
print(x)

# 4. TypeError: Occurs when an operation is performed on an object of inappropriate type.
# Example:
# print("Hello" + 10)  # Cannot concatenate string and integer
print("Hello" + str(10))

# 5. IndexError: Occurs when trying to access an index that does not exist in a sequence.
# Example:
# my_list = [1, 2, 3]
# print(my_list[3])  # Index 3 is out of range for my_list
my_list = [1, 2, 3]
print(my_list[2])

# 6. KeyError: Occurs when trying to access a key that does not exist in a dictionary.
# Example:
# my_dict = {'a': 1, 'b': 2}
# print(my_dict['c'])  # Key 'c' does not exist in my_dict
my_dict = {'a': 1, 'b': 2}
print(my_dict.get('c'))

# 7. ValueError: Occurs when a function receives an argument of correct type but with an inappropriate value.
# Example:
# x = int("abc")  # Cannot convert "abc" to an integer
try:
    x = int("123")
    print(x)
except ValueError:
    print("Invalid value")

# 8. FileNotFoundError: Occurs when trying to open a file that does not exist.
# Example:
# with open("nonexistent_file.txt") as f:
#     print(f.read())  # FileNotFoundError
with open("existing_file.txt") as f:
    print(f.read())

# 9. ZeroDivisionError: Occurs when attempting to divide by zero.
# Example:
# result = 10 / 0  # Division by zero
result = 10 / 2
print(result)
