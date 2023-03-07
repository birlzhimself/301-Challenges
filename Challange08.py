#!/usr/bin/python3

#Script Ops Challenge: Class 08 - Python Collections #Purpose Create a script that prints selected elements from the list #Why Learn how to make a list and print from the list

# Assigning a list of ten string elements to a variable my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "pear", "blueberry"]

# Printing the fourth element of the list print(my_list[3])

# Printing the sixth through tenth element of the list print(my_list[5:10])

# Changing the value of the seventh element to "onion" my_list[6] = "onion"

# Using some methods to manipulate the elements in the list my_list.append("kiwi") my_list.clear() my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "pear", "blueberry"] my_list.count("cherry") my_list.extend(["kiwi", "lemon", "mango"]) my_list.index("date") my_list.insert(4, "pineapple") my_list.pop() my_list.remove("elderberry") my_list.reverse() my_list.sort()

# Creating a tuple, a set, and a dictionary my_tuple = ("apple", "banana", "cherry") my_set = {"apple", "banana", "cherry"} my_dict = {"name": "Birlz", "age": 69, "city": "Lisbon"}
