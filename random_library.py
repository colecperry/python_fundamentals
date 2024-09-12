import random  # Import the random module

# Generate a random integer between 1 and 10 (inclusive)
print("\n")
random_int = random.randint(1, 10)
print("Random integer between 1 and 10:", random_int)
print("\n")

# Generate a random float between 0 and 1 <- You don't decide the args
random_float = random.random()
print("Random float between 0 and 1:", random_float)
print("\n")

# Generate a random float between 1 and 10 (inclusive) <- You decide the ags
random_uniform_float = random.uniform(1, 10)
print("Random float between 1 and 10:", random_uniform_float)
print("\n")

# Seed the random number generator for reproducibility, how answers below will stay the same
random.seed(42)

# Generate a random integer between 1 and 10 (inclusive) using the seeded random number generator
random_int_seeded = random.randint(1, 10)
print("Random integer between 1 and 10 using seeded generator:", random_int_seeded)
print("\n")

# Generate a random float between 0 and 1 using the seeded random number generator
random_float_seeded = random.random()
print("Random float between 0 and 1 using seeded generator:", random_float_seeded)
print("\n")
