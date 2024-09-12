# Dictionaries: keys must be strings or numbers, values can be anything
D = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
V = {'red': [1,0,0], 'cyan': [0,1,1]}
X = {1: 'one', 2: 'two', 3: 'three'}
Y = {'A': 'B', 1: 'C', 'D': 2}

# Keys and values
keys = D.keys()
print("Keys:", keys)  # Printing the keys of the dictionary D
values = D.values()
print("Values:", values)  # Printing the values of the dictionary D
print("\n")

# Delete a value in the dictionary
del D['X']
print("After deleting 'X':", D)  # Printing the dictionary D after deleting the key 'X'
print("\n")

# Check to see if a dictionary has a particular key
print("'I' in D:", 'I' in D)  # Checking if 'I' is a key in the dictionary D
print("'II' in D:", 'II' in D)  # Checking if 'II' is a key in the dictionary D
print("\n")

# Check if dictionary has a particular value using the values method
L = D.values()
print("5 in D.values():", 5 in L)  # Checking if 5 is a value in the dictionary D
print("\n")

# Extracting a value - must access by key, not index
a = D['V']
print("Value of 'V':", a)  # Printing the value associated with key 'V' in the dictionary D
print("\n")

# Adding an item to a Dictionary - this is the same as append for lists
D['D'] = 500
print("After adding 'D':", D)  # Printing the dictionary D after adding the key 'D' with value 500
print("\n")

# Changing the value of an item in a dictionary - cannot have two items with the same key
D['D'] = 501
print("After changing 'D' value:", D)  # Printing the dictionary D after changing the value of key 'D' to 501
print("\n")

# Make a copy of the dictionary
D2 = {'a': 10, 'b': 20, 'c': 30}
E = dict(D2)
D2['a'] = 100
print("D2 - After changing value of A:", D2)  # Printing the dictionary D2 after changing the value of key 'a'
print("E - copy of D2:", E)  # Printing the dictionary E which is a copy of D2 before the change
print("\nFor Loop:")

# Printing a for loop in a dictionary
for key in D2:
    print("key:", key, "value:", D2[key])  # Printing each key-value pair in the dictionary D2
print("\n")

# Creating a list of keys and values
key_list = [key for key in D2]
print("key list: ", key_list)

values_list = [D2[key] for key in D2]
print("values list: ", values_list)
print("\n.items():")

# .items() makes keys and values accessible independently of one another
my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

items_list = [item for item in my_dict.items()]
print("items list: ", items_list)
key_list_2 = [key for key, value in my_dict.items()]
print("key list: ", key_list_2)
values_list_2 = [value for key, value in my_dict.items()]
print("values list: ", values_list_2)
print("\n")

# .get method - .get method allows you to pass in a default value. Basically you are getting the key pair value for whatever you pass in to the .get method
dog = 'cuddly'

dict_map = {
    "hungry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "Playing tug of war.",
    "cuddly": "Snuggling."
}

owner = dict_map.get(dog)
print(owner)

owner_2 = dict_map.get("crazy", "Throw toy!")
print(owner_2)

owner_3 = dict_map.get("thirsty")
print(owner_3)




