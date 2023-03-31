class MyString(str):
    """
    A custom string class that inherits from the built-in str class.
    """

    def __init__(self, a: str) -> None:
        """
        Initializes a new instance of the my_string class.

        Args:
            a (str): The string to be converted into a my_string object.
        """
        super().__init__()
        self._list = list(a)

    def append(self, char: str) -> None:
        """
        Appends a character to the end of the string.

        Args:
            char (str): The character to be appended to the string.
        """
        self._list.append(char)

    def pop(self, index: int = -1) -> str:
        """
        Removes and returns the character at the specified index.

        Args:
            index (int, optional): The index of the character to be removed.
                If no index is specified, the last character is removed.

        Returns:
            The character that was removed from the string.
        """
        return self._list.pop(index)

    def __str__(self) -> str:
        """
        Returns the string representation of the my_string object.

        Returns:
            str: The string representation of the my_string object.
        """
        return ''.join(self._list)


# Creating an object of class my_string
s = MyString("PPytho")
print(s)

# The pop method is called on the s object with an argument of 0
# This removes the first character of the string ('P') and returns it
s.pop(0)
print(s)

# The append method is called on the s object with an argument of 'n'
# This adds the character 'n' to the end of the string
s.append('n')
print(s)
