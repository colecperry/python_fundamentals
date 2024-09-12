# The try block houses code that may generate a particular exception, and the except block is the code to execute if the particular exception is found
try:
    # Try to perform some operation that might raise an exception
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    # Handle the specific exception (division by zero) gracefully
    print("Error: Cannot divide by zero.")

except ValueError:
    # Handle the specific exception (invalid input) gracefully
    print("Error: Please enter valid integers.")

except Exception as e:
    # Handle any other exception that might occur
    print("An error occurred:", e)

finally:
    # Optional: Code that runs whether an exception occurred or not
    print("Thank you for using the calculator.")