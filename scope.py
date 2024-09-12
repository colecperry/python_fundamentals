# Global Scope
name = "Joe"
def greeting():
    print(f"Hello, {name}")

greeting()

# Local Scope - cannot access variable outside function
def local_scope():
    trapped_variable = "You can't access me outside this function"

# print(trapped_variable)

# Change global variable to local scope - notice how after running the function and printing the varible outside the function prints the old value
change_the_world = "change yourself"

def change_yourself():
    change_the_world = "world changed"


change_yourself()
print("running function and seeing if the value changed: ", change_the_world)

# Now use the global keyword
change_the_world_2 = "change yourself"

def change_yourself_2():
    global change_the_world_2
    change_the_world_2 = "world changed"

change_yourself_2()
print("running function and seeing if the value changed after using global: ", change_the_world_2)





