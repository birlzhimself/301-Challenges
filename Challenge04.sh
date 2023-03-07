!/bin/bash

#Script: Ops Challenge04: Conditionals in Menu Systems
#Purpose: Gives you an option
#Why: Because you deserve one!

while true; do
echo “Please select an option:”
echo “1. Hello world”
echo “2. Ping self”
echo “3. IP info”
echo “4. Exit”

read choice case $choice in 1) echo “Hello world!” ;; 2) ping -c 4 127.0.0.1 ;; 3) ifconfig ;; 4) exit 0 ;; *) echo “Invalid choice, please try again.” ;; esac
done
