#!/usr/bin/env python

import math

#The point to point function (ptop) measures the distance between a point and
#another using four number unput by the user
def ptop((x1, y1), (x2, y2)):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (y2 - y1)**2)
    return distance

#Gets four number from user input
x1 = int(raw_input("enter a number for x1: "))
y1 = int(raw_input("enter a number for y1: "))
x2 = int(raw_input("enter a number for x2: "))
y2 = int(raw_input("enter a number for y2: "))

#Prints the distance between the points
print "the distance between those points is: ", ptop((x1, y1), (x2, y2))

print "Thank you and Goodbye!"


# Distance formula
#   calculate a function called "distance" to calculate the distance between two points.
#   http://www.purplemath.com/modules/distform.htm
#   ex: 
#      >>> distance((0,0), (3,4))
#      5

# def distance(a, b):


# ADVANCED
# Normalizing Vectors
#   normalize a vector of length N.  If given all zeros, just spit back the same vector
#   http://www.fundza.com/vectors/normalize/index.html

#   ex:
#     >>> normalize((1,1))
#     [0.70710678118654746, 0.70710678118654746]
#     >>> normalize([0,0,0])
#     [0,0,0]
#     >>> normalize([1,1,1,1])
#     [0.25, 0.25, 0.25, 0.25]

# def normalize(vec):
