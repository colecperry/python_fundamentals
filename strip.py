# Demonstration of rstrip, lstrip, and strip methods in Python strings

# Example string with leading, trailing, and surrounding whitespace
text = "   Hello, world!   "

# rstrip() method removes trailing whitespace (by default) from the right end of the string
trimmed_right = text.rstrip()
print("After rstrip():", trimmed_right)  # Output: "   Hello, world!"

# lstrip() method removes leading whitespace (by default) from the left end of the string
trimmed_left = text.lstrip()
print("After lstrip():", trimmed_left)  # Output: "Hello, world!   "

# strip() method removes leading and trailing whitespace (by default) from the string
trimmed_both = text.strip()
print("After strip():", trimmed_both)  # Output: "Hello, world!"

# Additional examples with custom characters

# Example string with custom characters
text_with_chars = "!!!Hello, world!!!"

# rstrip() with custom characters removes trailing exclamation marks
trimmed_right_custom = text_with_chars.rstrip("!")
print("After rstrip('!'):", trimmed_right_custom)  # Output: "!!!Hello, world"

# lstrip() with custom characters removes leading exclamation marks
trimmed_left_custom = text_with_chars.lstrip("!")
print("After lstrip('!'):", trimmed_left_custom)  # Output: "Hello, world!!!"

# strip() with custom characters removes leading and trailing exclamation marks
trimmed_both_custom = text_with_chars.strip("!")
print("After strip('!'):", trimmed_both_custom)  # Output: "Hello, world"

