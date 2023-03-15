#!/usr/bin/python3

#Script:   Ops Challenge: Class 10 - Python Collections 
#Purpose:  Create if statements using these logical conditionals
#Why:      Learn how to print information to the screen depending on if the condition is met.

import os

# Create a new file
with open("example.txt", "w") as f:
    # Append three lines
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

# Read and print the first line
with open("example.txt", "r") as f:
    first_line = f.readline()
    print(first_line)

# Delete the file
os.remove("example.txt")
