# Conditional Expressions - evaluate the truthiness of complex statements in a single line
# follows format: value_if_true if condition else value_if_false

age = 1
is_baby = 'baby'if age < 2 else 'not a baby'

# This is equivalent to:
age = 1
if age < 2:
    is_baby = 'baby'
else:
    is_baby = 'not a baby'

