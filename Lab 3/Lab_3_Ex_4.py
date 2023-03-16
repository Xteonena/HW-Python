class my_string(str):
    def __init__(self, a):
        super().__init__()
        self._list = list(a)

    def append(self, char):
        self._list.append(char)

    def pop(self, index=-1):
        return self._list.pop(index)

    def __str__(self):
        return ''.join(self._list)


# Creating an object of class my_string
s = my_string("PPytho")
print(s)

# The pop method is called on the s object with an argument of 0
# This removes the first character of the string ('P') and returns it
s.pop(0)
print(s)

# The append method is called on the s object with an argument of 'n'
# This adds the character 'n' to the end of the string
s.append('n')
print(s)
