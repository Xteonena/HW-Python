# This code calculates the factorial of a number using a loop.

# Define a function that calculates the factorial of a number using a loop
def fac_loop(n):
    # Initialize a variable to store the result
    result = 1

    # Loop over the range from 1 to "n" + 1
    for i in range(1, n + 1):
        # Multiply the result by the current value of "i"
        result *= i

    # Return the final result
    return result


# Define a function that prompts the user for a number and returns the result of "fac_loop"
def fac_loop_input():
    # Prompt the user for a number and convert the input to an integer
    n = int(input("Enter a number: "))

    # Call the "fac_loop" function and return the result
    return fac_loop(n)


# Call the "fac_loop_input" function and print the result
print(fac_loop_input())
