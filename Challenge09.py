#!/usr/bin/python3

#Script:   Ops Challenge: Class 09 - Python Collections 
#Purpose:  Create if statements using these logical conditionals
#Why:      Learn how to print information to the screen depending on if the condition is met.

a = 10
b = 5

if a == b:
    print("a is equal to b")
if a != b:
    print("a is not equal to b")
if a < b:
    print("a is less than b")
if a <= b:
    print("a is less than or equal to b")
if a > b:
    print("a is greater than b")
if a >= b:
    print("a is greater than or equal to b")

    
   #stretch
  
a = 10
b = 5

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
