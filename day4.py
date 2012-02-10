#!/usr/bin/env python

count=0
while count <=0:
    count=raw_input("Count down from what: ")
    count=int(count)

while count>0: 
    print count
    count-=1

print "Blastoff!"
