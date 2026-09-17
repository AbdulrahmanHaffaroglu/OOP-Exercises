'''
Create a Rectangle class with:

width
height

Methods:

area()
perimeter()
is_square()

Then create a Square class.
'''

class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def is_square(self):
        return self._width == self._height

    def width_setter(self, width):
        self._width = width

    def height_setter(self, height):
            self._height = height

    def width_getter(self):
        return self._width

    def height_getter(self):
        return self._height

    width = property(fget=width_getter, fset=width_setter)
    height = property(fget=height_getter, fset=height_setter)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    
    def width_setter(self, width):
        self._width = width
        super().height_setter(width)

    def height_setter(self, height):
        self._height = height
        super().width_setter(height)

    width = property(fset=width_setter)
    height = property(fset=height_setter)
        
            


s1 = Square(20)
s2 = Square(10)

print(s1.area())
print(s2.area())

s1.width_setter(10)

print(s1.perimeter())
print(s2.perimeter())

print(s1.is_square())
print(s2.is_square())
