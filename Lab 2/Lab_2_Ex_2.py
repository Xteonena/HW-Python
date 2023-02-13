# This code calculates and returns the result of raising a number to a power

# Define a function that prompts the user for a number and a power, and returns the result of raising the number to
# the power

def new_power():
    # Prompt the user for a number and convert the input to an integer
    a = int(input("Enter the number: "))

    # Prompt the user for a power and convert the input to an integer
    b = int(input("Enter the power: "))

    # Calculate the result of raising "a" to the power of "b"
    result = a ** b

    # Return a string that concatenates the input, the operation, and the result
    return "The number " + str(a) + " to the power of " + str(b) + " = " + str(result)


# Call the "new_power" function and print the result
print(new_power())
