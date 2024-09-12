# List Comprehensions:
    # Creates a list, performs a for loop, stores and evaluates the list in memory. 

player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

inch_heights = [height * 7920 for height in player_heights]

print("player heights: ", player_heights)
print("inch heights: ", inch_heights)

# this is the same as: 
# inch_heights = list()
# for height in player_heights:
#     inch_height = height * 7920
#     inch_heights.append(inch_height)

# Can also create a list and perform a loop all in one step:
squared = [(n**2)for n in range(1,11)]
print("squared: ", squared)

# Generator expressions:
    # Creates a generator object and does not store them in memory, and the items are generated one at a time as needed

squared_2 = ((n**2) for n in range(1,11))
print("squared_2: ", squared_2)