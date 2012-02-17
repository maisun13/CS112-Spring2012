#!/usr/bin/env python

total = 0
input_list = []
input_number = None

#get list of numbers from user
while input_number != "":
    input_number = raw_input()
    if input_number.isdigit():
        var2.append(float(input_number))

#total the list of numbers
total = 0
for num in input_list:
    total += num

#print average of list
print total/len(input_list)
