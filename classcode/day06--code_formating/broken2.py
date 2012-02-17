#!/usr/bin/env python

from random import randint

s=1
input_number=int(raw_input())
list1=[]

for _ in range(input_number):
    list1.append(randint(0,20))

print list1

while s:
    s=0
    for num in range(1,input_number):
        if list1[num-1]>list1[num]:
            input_number1=list1[i-1]
            input_number2=list1[i]
            list1[i-1]=input_number2
            list1[i]=t1
            s=1
print list1
