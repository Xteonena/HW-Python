import string

sentence = "I am@Python@senior^pomidor"

list_with_words = sentence.split()

new_list = [word for word in list_with_words if word not in string.punctuation]
'''

This refactored version uses a list comprehension to create
the final new_list by filtering the words that are in the string.punctuation list 

'''
print(new_list)
# This approach is more concise and easier to read than the original version
