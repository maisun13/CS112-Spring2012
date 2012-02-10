#!/usr/bin/env python
from hwtools import *

print "Section 2:  Loops"
print "-----------------------------"

# 1. Keep getting a number from the input (num) until it is a multiple of 3.

print "1.", 
num = float (raw_input("Enter a number that is divisible by 3 please!: "))
while (num%3) != 0:
    num = float(raw_input("Try again please!: "))

print "2. Countdown From:",
while num>0:
    print num
    num-=3

print "BRASTOFF!!!"
   


