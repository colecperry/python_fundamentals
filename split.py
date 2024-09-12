# Demonstrating the split() method in Python strings

# Example string to split
text = "Hello, world! This is a sample string."

# Using split() without any arguments
# Splits the string at whitespace characters by default
words = text.split()
print("Splitting at whitespace characters:", words)
# Output: ['Hello,', 'world!', 'This', 'is', 'a', 'sample', 'string.']

# Using split() with a custom delimiter
# Splits the string at commas
words_comma = text.split(",")
print("Splitting at commas:", words_comma)
# Output: ['Hello', ' world! This is a sample string.']

# Using split() with a custom delimiter and maxsplit argument
# Splits the string at the first occurrence of a space, with at most 1 split
words_first_space = text.split(" ", 1)
print("Splitting at the first space:", words_first_space)
# Output: ['Hello,', 'world! This is a sample string.']

# Using rsplit() with a custom delimiter and maxsplit argument
# Splits the string at the last occurrence of a space, with at most 1 split
words_last_space = text.rsplit(" ", 1)
print("Splitting at the last space:", words_last_space)
# Output: ['Hello, world! This is a sample', 'string.']
