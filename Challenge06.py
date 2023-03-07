#!/usr/bin/python3

#Script Ops Challenge: Class 06 - Bash in Python 
#Purpose Create a python script that executes bash commands, saves them as variables and outputs them to the terminal. 
#Why Learn how to import a module, save bash commands output as a variable and print it to the terminal.

import os

whoami_output = os.popen(‘whoami’).read()

ip_output = os.popen(‘ip a’).read()

lshw_output = os.popen(‘lshw -short’).read()

print(“Output of whoami command:\n”, whoami_output) 
print(“Output of ip a command:\n”, ip_output) 
print(“Output of lshw -short command:\n”, lshw_output)

import subprocess

whoami_output = subprocess.run([‘whoami’], capture_output=True, text=True).stdout

ip_output = subprocess.run([‘ip’, ‘a’], capture_output=True, text=True).stdout

lshw_output = subprocess.run([‘lshw’, ‘-short’], capture_output=True, text=True).stdout

print(“Output of whoami command:\n”, whoami_output) 
print(“Output of ip a command:\n”, ip_output) 
print(“Output of lshw -short command:\n”, lshw_output)
