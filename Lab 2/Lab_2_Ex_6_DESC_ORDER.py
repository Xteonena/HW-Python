# This code sorts the keys of a dictionary based on their values and prints the sorted keys

# Create a dictionary with 4 key-value pairs
dictionary = {'b': 3, 'c': 2, 'a': 4, 'd': 1}

# Convert the keys of the dictionary to a list
keys = list(dictionary.keys())

# Sort the keys of the list based on the values of the dictionary in descending order
keys.sort(key=lambda x: dictionary[x], reverse=True)

# Print the sorted keys
print(keys)
