import random

list_with_numbers = list(range(10))

new_list = [i + random.random() for i in list_with_numbers if not i % 2]
'''

This version eliminates the need for a for loop and an intermediate new_list. 
Instead, it directly generates the final list using a list generator that filters and 
displays the elements on the same line

'''
print(new_list)
# This refactored version is more concise and easier to read
