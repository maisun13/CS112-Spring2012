#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)

print "1.",
if n % 2 == 0 :
    print n, "is an even number"
else:
    print n, "is an odd number"


# 2. If n is odd, double it
print "2.",
if n % 2 == 0 :
    print n
else:
    print n*2


# 3. If n is evenly divisible by 3, add four
print "3.",
if n % 3 == 0 :
    print n+4
else:
    print n
    


# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)

print "4.",
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"
print letter

