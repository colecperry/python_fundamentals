# Set a breakpoint to the left of the line using the red dot - that's where the code will stop running
# We then want to select 'run and debug' from the left side terminal, click it, and select python debugger
    # On the left, you can see all the local and global variables
    # The top menu has buttons to:
    # continue(to next breakpoint)
    # Step over: executes the current line of code and moves to the next line, but if the current line contains a function call, it will execute the entire function in a single step. Useful for when you want to skip over function calls without getting into their internal details.
    # Step into: If the current line of code contains a function call, the debugger will move into the first line of the called function, allowing you to continue debugging inside the function. If the current line does not contain a function call, it behaves like "step over." Useful for when you want to inspect behavior of a function call in detail
    # Step out: Completes the execution of the current function and returns to calling the function. The debugger will pause at the line of code immediately after the function call. Useful for when you are inside a function and have finished inspecting it's behavior.
    # Restart - rerun
    # Stop
# Watch - type in manually which variables to watch, and observe their values

# Directions to practice debugging
    # Set a breakpoint at the line result_add = add(x, y) in the main function.
    # Optionally, set breakpoints inside the add and multiply functions to practice "Step Out."
    # Practice Step Into -> When the debugger hits the breakpoint at result_add = add(x, y), press F11 (Step Into) to move into the add function.
    # Practice Step Over -> After stepping into and finishing the add function, the debugger will return to the main function. When the debugger is at the line result_multiply = multiply(x, y), press F10 (Step Over) to execute the multiply function without stepping into it.
    # Practice Step Out -> Set a breakpoint inside the multiply function. Use "Step Into" to enter the multiply function, then press Shift+F11 (Step Out) to complete the function execution and return to the caller.
    # Nested Function calls -> Set a breakpoint at the line combined_result = add(result_add, multiply(x, y)). Use "Step Into" and "Step Out" to practice navigating through nested function calls.


def multiply(a, b):
    product = a * b 
    return product # <- Set breakpoint here

def add(a, b):
    sum = a + b 
    return sum # <- Set breakpoint here

def main():
    x = 10
    y = 20

    # Step into this function call to see its internals
    result_add = add(x, y) # <- Set breakpoint here

    # Step over this function call to skip its internals
    result_multiply = multiply(x, y)

    # Print the results
    print(f"Sum: {result_add}")
    print(f"Product: {result_multiply}")

    # Nested function calls to practice stepping in and out
    combined_result = add(result_add, multiply(x, y))
    print(f"Combined Result: {combined_result}")

if __name__ == "__main__":
    main()