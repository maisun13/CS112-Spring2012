#!/usr/bin/env python
from hwtools import *

tot_num = 0
has_odds = False

odd_nums_under_benjies = []
even_nums = []

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?

print "1.", 

for indiv_num in nums :
	tot_num = tot_num + indiv_num
	if indiv_num % 2 == 0 :
		even_nums.append (indiv_num)
	else :
		has_odds = True
		if indiv_num < 100 :
			odd_nums_under_benjies.append (indiv_num)

print (tot_num)


# 2. Print every even number in nums

print "2. ",

print (even_nums)

# 3. Does nums only contain even numbers? 

print "3.",
if has_odds:
    print "some odd"
else:
    print "even only"


# 4. Generate a list every odd number less than 100. Hint: use range()

print "4.", 

if has_odds :
	print (odd_nums_under_benjies)
else:
	print "no odd numbers"



