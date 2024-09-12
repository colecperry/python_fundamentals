# Print out a simple for loop - you don't choose how many times to loop
s1 = 'abcd'
for char in s1:
    print(char)
print("\n")

# Reverse a string with foor loop
s2 = 'xyz'
t = ''
for char in s2:
    t = char + t
    print(t)
print("\n")

# Print out a range loop - you choose how many times to loop
# k is the loop variable that starts at 0 if no other arguments passed
n = 4
for k in range(n):
    print(k)
print("\n")

# Example with multiple arguments:
for k in range(3, 12, 3):
    print(k)
print("\n")

# Example going backwards:
for k in range(5, 0, -1):
    print(k)
