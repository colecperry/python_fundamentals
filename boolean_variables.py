# Example of a boolean variable
Y = int(input("Enter a 4 digit year: "))
CenturyYear = (Y % 100 == 0)
print(CenturyYear)

L = 1
R = 2
x = 1.3
inside = (L<=x and x<=R)
print(inside)