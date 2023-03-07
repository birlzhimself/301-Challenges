#!/bin/bash/

#Script:     Ops Challenge: Class 02 – Append; Date and Time
#Purpose:    This script copies the /var/log/journal to the current working directory and prints the date
#Why:        Learn to write and complete Bash Files

#Create Variable
timestamp=$(date “+%Y-%m-%d_%H:%M:%S”)

echo $timestamp

#Copy Log into Current Directory
if cp -r /var/log/journal ./journal_$timestamp;then
echo “Great Sucess!”

else

Echo “Computer says No”

fi
