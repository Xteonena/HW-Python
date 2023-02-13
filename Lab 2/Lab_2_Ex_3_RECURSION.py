# This code calculates the factorial of a number using recursion.

# Define a function that calculates the factorial of a number using recursion
def fac_recursion(n):
    # If "n" is equal to 0, return 1
    if n == 0:
        return 1

    # Otherwise, return "n" multiplied by the result of a recursive call to "fac_recursion" with "n" decremented by 1
    return n * fac_recursion(n - 1)


# Define a function that prompts the user for a number and returns the result of "fac_recursion"
def fac_recursion_input():
    # Prompt the user for a number and convert the input to an integer
    n = int(input("Enter a number: "))

    # Call the "fac_recursion" function and return the result
    return fac_recursion(n)


# Call the "fac_recursion_input" function and print the result
print(fac_recursion_input())
