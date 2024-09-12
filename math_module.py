# Showcase of useful functions from the math module

import math

# Ceiling function (cil)
x = 3.4
ceil_result = math.ceil(x)
print("Ceiling of", x, ":", ceil_result)

# Floor function (floor)
y = 5.9
floor_result = math.floor(y)
print("Floor of", y, ":", floor_result)

# Square root function (sqrt)
z = 16
sqrt_result = math.sqrt(z)
print("Square root of", z, ":", sqrt_result)

# Exponential function (exp)
a = 2
exp_result = math.exp(a)
print("Exponential of", a, ":", exp_result)

# Natural logarithm function (log)
b = 10
log_result = math.log(b)
print("Natural logarithm of", b, ":", log_result)

# Base 10 logarithm function (log10)
c = 100
log10_result = math.log10(c)
print("Base 10 logarithm of", c, ":", log10_result)

# Sine function (sin)
angle = math.pi / 2
sin_result = math.sin(angle)
print("Sine of", angle, ":", sin_result)

# Cosine function (cos)
cos_result = math.cos(angle)
print("Cosine of", angle, ":", cos_result)

# Find out what's in a module?
# print(help('math'))
# print(help('math.sqrt'))