#!/bin/bash

#Spript Ops Challenge: Class 03 – Change Permissions
#Purpose Change user premissions
#Why Because that’s the challenge!

#Prompt the user for the directory path
read -p "Enter the directory path: " directory_path

#Prompt the user for the permissions number
read -p "Enter the permissions number: " permissions

#Change the directory to the input path
cd “$directory_path”

#Change the permissions of all files in the directory
chmod -R “$permissions” .

#Print the directory contents and permissions
echo “Directory contents:”
ls -l

#Stretch goal: output a log file of all actions taken by the script
echo “Script actions:” >> script.log
echo “Changed directory to: $directory_path” >> script.log
echo “Changed permissions to: $permissions” >> script.log
echo “Directory contents:” >> script.log
ls -l >> script.log

#Stretch goal: output each file changed one by one, with a slight delay between each file
for file in *
do
echo “Changing permissions of file: $file”
sleep 1
chmod “$permissions” “$file”
done
