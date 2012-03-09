#!/usr/bin/env python
import math 

class Point(object):
    # Initializes the code
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Calculates the distance between two points
    def distance(self, other):
        distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return distance
    # Sets the points location to x and y
    def move(self, x, y):
        self.x = self.x = x
        self.y = self.y = y

    # Offsets the point by x and y
    def translate(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
        
# Defines the two points      
a = Point(1, 1)
b = Point(2, 2)
# Prints the location of the points
print a.x, a.y
print b.x, b.y
# Prints the distance between the points a and b
print a.distance(b)
# Moves the points a and b to the specified point
a.move(2, 2)
b.move(1, 1)
# Prints the new location of the points
print a.x, a.y
print b.x, b.y
# Offsets the points by x and y
a.translate(4, 4)
b.translate(6, 6)
# Prints the new location of the points
print a.x, a.y
print b.x, b.y





