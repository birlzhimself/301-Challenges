!/usr/bin/python3

#Script:   Ops Challenge: Class 11 - Python Collections 
#Purpose:  Use Psutil to fetch system information.
#Why:      Learn how to use Psutil

import psutil

# Get the CPU times for the system
cpu_times = psutil.cpu_times()

# Print the CPU times to the screen
print("CPU Times:")
print(f"User Mode: {cpu_times.user:.2f} seconds")
print(f"Kernel Mode: {cpu_times.system:.2f} seconds")
print(f"Idle Time: {cpu_times.idle:.2f} seconds")
print(f"Priority User Mode: {cpu_times.nice:.2f} seconds")
print(f"I/O Wait Time: {cpu_times.iowait:.2f} seconds")
print(f"Hardware Interrupt Time: {cpu_times.irq:.2f} seconds")
print(f"Software Interrupt Time: {cpu_times.softirq:.2f} seconds")
print(f"Virtual OS Time: {cpu_times.steal:.2f} seconds")
print(f"Virtual CPU Time: {cpu_times.guest:.2f} seconds")

#Stretch Goal
#Saves the information into a text file
with open("cpu_times.txt", "w") as file:
    file.write("CPU Times:\n")
    file.write(f"User Mode: {cpu_times.user:.2f} seconds\n")
    file.write(f"Kernel Mode: {cpu_times.system:.2f} seconds\n")
    file.write(f"Idle Time: {cpu_times.idle:.2f} seconds\n")
    file.write(f"Priority User Mode: {cpu_times.nice:.2f} seconds\n")
    file.write(f"I/O Wait Time: {cpu_times.iowait:.2f} seconds\n")
    file.write(f"Hardware Interrupt Time: {cpu_times.irq:.2f} seconds\n")
    file.write(f"Software Interrupt Time: {cpu_times.softirq:.2f} seconds\n")
    file.write(f"Virtual OS Time: {cpu_times.steal:.2f} seconds\n")
    file.write(f"Virtual CPU Time: {cpu_times.guest:.2f} seconds\n")
    
    
