#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

while True:
    try:
        nums = input_nums() # User inputs a list of numbers. 

        # To find any duplicate numbers.
        for num in nums:
            if nums.count(num) > 1:
                raise NameError ('duplicate')
        break

    # Print an error statement if the user inputs something other than a number.
    except ValueError:
        print "Please enter numers."

    # Print an error statement if the user inputs any duplicate numbers.     
    except NameError:
        print "No repeating numbers please!"


nums_sort = sorted(nums) # User's sumbers are sorted into a list.
print "I have sorted your numbers"
print nums_sort

while True:
    try:
        # User inputs a number to find in the list.
        num_to_find = int(raw_input("Which number should I find: "))
        break
    # Print an error statement if user enters anything other than a number.
    except ValueError:
        print "Enter a number please."

min_position = 0 # The minimum position in the list being checked. 

max_position = len(nums_sort) - 1 # The maximum position in the list being checked.

mid_position = (min_position + max_position) / 2 # The middle position in the list being checked. This is found by getting the average of the minimum and maximum position).

# While the number to find is not equal to the middle position or if te minimum position is less than the maximum position:
while (nums_sort[mid_position] != num_to_find) or (min_position < max_position):

    # Check the posiiton to the right if the number to find is greater than the middle position (add one to the middle position).
    if num_to_find > nums_sort[mid_position]:
        min_position = mid_position + 1 

        # Check the middle position again. 
        mid_position = (min_position + max_position) / 2
    # Check the position to the left if the number to find is less than the middle position (subtract one from the middle position).
    elif num_to_find < nums_sort[mid_position]:
        max_position = mid_position - 1

        # Check the middle position again. 
        mid_position = (min_position + max_position) / 2

    # Break the while loop if the middle position matches the number to find or if the minimum position becomes greater than the maximum position. 
    if (nums_sort[mid_position] == num_to_find) or (min_position > max_position):
        break

# If the middle position is equal to the number to find then print the the number to find has been found at it's position in the list. 
if (nums_sort[mid_position] == num_to_find):
    print "Found", num_to_find, "at position", mid_position + 1 , "in sorted list"

# Print that the number couldn't be foun if the number could not be found at all. 
else:
    print "Could not find", num_to_find
