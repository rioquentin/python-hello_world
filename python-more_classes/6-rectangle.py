#!/usr/bin/python3
''' Empty Class'''


class Rectangle:
    '''Property of class rectangle'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''return area'''
        return self.height * self.width

    def perimeter(self):
        '''return  perimeter'''
        if self.height == 0 or self.width == 0:
            return 0
        return self.height * 2 + self.width * 2

    def __str__(self):
        '''print rectangle'''
        l = ""
        if self.height == 0 or self.width == 0:
            return l
        for i in range(0, self.height):
            for x in range(0, self.width):
                l += "#"
            if i + 1 != self.height:
                l += "\n"
        return l

    def __repr__(self):
        '''return repres'''
        a = ("Rectangle({}, {})".format(self.width, self.height))
        return a

    def __del__(self):
        '''return del message'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
