# This code sorts a list of tuples based on the value of the third element in each tuple.

# Define a list of tuples
list_of_tuples = [(1, 1, 1), (1, 2, 3), (-1, -1, 7), (-3, -2, 8), (0, 0, 0), (3, -4, -5)]

# Sort the list of tuples based on the third element in each tuple
# The "sorted" function takes the list of tuples and a key function as arguments
# The key function is defined as a lambda expression that accesses the third element in each tuple (index 2)
# The "sorted" function returns a new list, sorted in ascending order based on the result of the key function
sorted_list = sorted(list_of_tuples, key=lambda x: x[2])

# Print the sorted list of tuples
print(sorted_list)