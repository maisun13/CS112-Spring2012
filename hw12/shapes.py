#!/usr/bin/env python
import math

class Shape(object):
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        Shape.__init__(self)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width*2 + self.height*2

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def circumference(self):
        return (self.radius*2) * math.pi
   
    

