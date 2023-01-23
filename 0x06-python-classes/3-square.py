#!/usr/bin/python3                                                                    
"""A module defines a square based on task 1(1-square.py                                   
"""                                                                                                                                                                             

class Square:                                                                              
    """A Square class that checks for tyeerror and valueerror                              
    """                                                                                    
    def __init__(self, size=0):              
        """class initialisation                                                            
        """                                                                                
        if not isinstance(size, int):                                                      
            raise TypeError('size must be an integer')                                     
        else:                                                                              
            if size < 0:                                                                   
                raise ValueError("size must be >= 0")                                      
            else:                                                                          
                self.__size = size

    def area(self):
        """a method that defines the are/a of the square
        Returns:
            int: the area of the square
        """
        return self.size ** 2
