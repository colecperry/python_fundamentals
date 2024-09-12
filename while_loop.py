# Use a while loop when you don't know how many iterations you will need
k = 0
s = 0
while k < 5:
    k = k + 1
    s = s + k
    print(k,s)

# Example of a while loop in error handling:
# Initialize a variable to keep track of whether the user has entered a valid number
valid_input = False

# Keep asking the user for a number until they enter a valid one
while not valid_input:
    try:
        # Ask the user to input a number
        number = float(input("Enter a number greater than 10: "))
        
        # Check if the number is greater than 10
        if number > 10:
            valid_input = True  # Set valid_input to True to exit the loop
        else:
            print("Number must be greater than 10. Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print("Valid input received. Exiting the loop.")

# Up down sequence problem
n = int(input('m= '))
m = n
nSteps = 0
maxSteps = 200
while m > 1 and nSteps < maxSteps:
    if m%2==0:
        m = m/2
else:
    m = 3*m + 1
nSteps = nSteps+1
print(n,nSteps,m)

# Print an infinite loop
# while True:
#     print("Infinte loop")