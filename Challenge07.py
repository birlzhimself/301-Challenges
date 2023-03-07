#!/usr/bin/python3

#Script:    Ops Challenge: Class 07
#Purpose:   Create a Python script that generates all directories, sub-directories and files for a user-provided directory path. 
#Why:       Learn how to import OS sistem to Script

import os

def generate_directory_info(path):
    for root, dirs, files in os.walk(path):
        print(f"Root: {root}")
        print(f"Directories: {dirs}")
        print(f"Files: {files}\n")

def create_test_directory(name):
    os.makedirs(name)
    for i in range(1, 4):
        subdir = f"{name}_0{i}"
        os.makedirs(os.path.join(name, subdir))

if __name__ == "__main__":
    user_input = input("Enter directory path: ")
    generate_directory_info(user_input)
    create_test_directory("testdir")

    python script.py > output.txt
