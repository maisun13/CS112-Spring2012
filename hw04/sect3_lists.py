#!/usr/bin/env python
from hwtools import *

print "Section 3:  Lists"
print "-----------------------------"

nums = input_nums()
# 1. "nums" is a list of numbers entered from the command line.  How many
#    numbers were entered?

print "1.",

print len (nums)
listtotal = len (nums)

# 2.  Append 3 and 5 to nums

print "2.", 

nums.append (3)
nums.append (5)
print (nums)

# 3.  Remove the last element from nums

print "3.", 

nums.pop ()

# 4.  Set the 3rd element to 7

print "4.", 

nums[3]=7
print nums


# 5. [ADVANCED] Grab a new list of numbers and add it to the existing one

# print "5.", nums


# 6. [ADVANCED] Make a copy of this new giant list and delete the 2nd 
#    through 4th values

# nums_copy = __
# print "6.", nums, nums_copy

# 7-9. [ADVANCED] Print the following:

# print "7.", nums[__]    # first 3 elements
# print "8.", nums[__]    # last element
# print "9.", nums[__]    # a list of the second element
