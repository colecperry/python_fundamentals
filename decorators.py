# # Decorators - help reduce the amount of code that you need to write in your application

# # Code without decorators
# def sweep_floors(time):
#     if 1100 < time < 2100:
#         print("Sweeping the floors...")
#     else:
#         print("I'm off duty!")

# def wash_dishes(time):
#     if 1100 < time < 2100:
#         print("Washing the dishes...")
#     else:
#         print("I'm off duty!")

# def chop_vegetables(time):
#     if 1100 < time < 2100:
#         print("Chopping the vegetables...")
#     else:
#         print("I'm off duty!")

# Code with decorators
def check_working_hours(func): # Decorator takes a function as an arg and returns a new function 'wrapper'
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            print("I'm off duty!")
    return wrapper

@check_working_hours # Each function is passed to the check_working_hours decorator
def sweep_floors(time):
    print("Sweeping the floors...")

@check_working_hours
def wash_dishes(time):
    print("Washing the dishes...")

@check_working_hours
def chop_vegetables(time):
    print("Chopping the vegetables...")


# When @check_working_hours is applied to 'sweep_floors', it is equivalent to:
    # sweep_floors = check_working_hours(sweep_floors)
    # When you decorate a function with @check_working_hours, it’s equivalent to passing that function to check_working_hours and then assigning the result back to the original function name.
    # AKA, when you call sweep_floors(800), it actually calls wrapper(800)
sweep_floors(800)
wash_dishes(1000)
chop_vegetables(1200)