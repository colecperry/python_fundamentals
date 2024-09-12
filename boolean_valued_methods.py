# Define a string with various types of characters
text = "Hello123"
print("Original text:", text)

# Check if all characters are lowercase
if text.islower():
    print("The text contains only lowercase letters.")
else:
    print("The text contains uppercase letters or non-alphabetic characters.")

# Check if all characters are uppercase
if text.isupper():
    print("The text contains only uppercase letters.")
else:
    print("The text contains lowercase letters or non-alphabetic characters.")

# Check if all characters are alphanumeric
if text.isalnum():
    print("The text contains only alphanumeric characters.")
else:
    print("The text contains non-alphanumeric characters.")

# Check if all characters are alphabetic
if text.isalpha():
    print("The text contains only alphabetic characters.")
else:
    print("The text contains non-alphabetic characters or digits.")

# Check if all characters are digits
if text.isdigit():
    print("The text contains only digits.")
else:
    print("The text contains non-digit characters or alphabetic characters.")
