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


import json

# Open the pfSense configuration file
with open("config.xml", "r") as f:
    config = f.read()

# Modify a value in the configuration file
config_json = json.loads(config)
config_json["some_setting"] = "new_value"
modified_config = json.dumps(config_json)

# Save the modified configuration to a new file
with open("modified_config.xml", "w") as f:
    f.write(modified_config)

# Import the modified configuration to pfSense
# (this assumes you have a way to import configurations to pfSense programmatically)
import_config("modified_config.xml")
