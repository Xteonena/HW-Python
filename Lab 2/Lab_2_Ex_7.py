# This code defines a decorator called "johnsonic", which takes a function as an argument and returns a new function
# that wraps the original function. The purpose of the "johnsonic" decorator is to format the output of the original
# function as a JSON string.

import json


# Define the johnsonic decorator function
def johnsonic(func):
    # Define the wrapper function, which takes in any number of positional and keyword arguments
    def jsonity(*args, **kwargs):
        # Call the original function with the passed arguments
        result = func(*args, **kwargs)
        # Format the result as a JSON string and return it
        return json.dumps(result)

    # Return the wrapper function as the result of the "johnsonic" decorator
    return jsonity


# Decorate the get_animal_name function with the "johnsonic" decorator
@johnsonic
def get_animal_name(number, animalss):
    # Return a dictionary with a key "animal_name" and a value from the "animals" list based on the "number" argument
    return {"animal_name": animalss[number]}


# Define a list of animals
animals = ["dog", "cat", "pig", "bird"]

# Prompt the user to enter a number
animal_number = int(input("Enter the number of the animal: "))

# Call the get_animal_name function and print the result
print(get_animal_name(animal_number, animals))
