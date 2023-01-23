#!/usr/bin/python3
"""creates class Square."""

class Square:
    """a square class defined
    Attributes:
        size (int): size of the square
        position(tuple: position ofspaces and lines
    """
    def __init__(self, size=0, position=(0, 0)):
        """class instance initialisation 
        Args:
            size (int): size
            position (tuple): position
        Return:
            nothing
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        getter of size
        Return:
            size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the vslue of size
        Args:
            value (int)
        Raises:
            TypeError: if size is not int
            ValueError: if size is >= 0
        Return:
            None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be <= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter for position
        returns:
            none
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of position
        Args:
            value (tuple)
        Returns:
            none
        """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        get area
        Return:
            area (int)
        """
        return self.__size ** 2

    def my_print(self):
        """
        print a square
        Returns:
            None
        """
        if self.size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)
