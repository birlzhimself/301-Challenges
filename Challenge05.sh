#!/bin/bash

#Script         Challange05
#Purpose        Zip content of backup directory
#Why            Because I said so...

# Get the current date and time in the desired format
timestamp=$(date +%Y%m%d%H%M%S)

# Create the backup directory if it doesn't already exist
backup_dir="/var/log/backups"
if [ ! -d "$backup_dir" ]; then
    mkdir "$backup_dir"
fi

# Get the file size of the log files before compression
syslog_size=$(du -h /var/log/syslog | awk '{print $1}')
wtmp_size=$(du -h /var/log/wtmp | awk '{print $1}')

# Compress the log files and save them to the backup directory
zip -j "$backup_dir/syslog-$timestamp.zip" /var/log/syslog
zip -j "$backup_dir/wtmp-$timestamp.zip" /var/log/wtmp

# Clear the contents of the log files
echo "" > /var/log/syslog
echo "" > /var/log/wtmp

# Get the file size of the compressed files
syslog_backup_size=$(du -h "$backup_dir/syslog-$timestamp.zip" | awk '{print $1}')
wtmp_backup_size=$(du -h "$backup_dir/wtmp-$timestamp.zip" | awk '{print $1}')

# Print the file size of the log files before and after compression
echo "Original syslog file size: $syslog_size"
echo "Original wtmp file size: $wtmp_size"
echo "Compressed syslog file size: $syslog_backup_size"
echo "Compressed wtmp file size: $wtmp_backup_size"

# Compare the size of the compressed files to the size of the original log files
if (( $(echo "$syslog_backup_size < $syslog_size" | bc -l) )) && (( $(echo "$wtmp_backup_size < $wtmp_size" | bc -l) )); then
    echo "Compression successful"
else
    echo "Compression failed"
fi

# Stretch Goals
# Clearing tracks
# To clear tracks using this script, one can simply execute it after performing the activity they want to cover up. The script will clear the logs and compress them, effectively removing any evidence of the activity from the system.

# Clearing other system logs
# Here's an updated script that clears some additional system logs. I've included comments explaining what each log tracks and why it's important.

# Clear the system message log
echo "" > /var/log/messages
echo "Cleared system message log"

# The system message log (/var/log/messages) tracks various system messages, including kernel messages, service start/stop messages, and more. This log can be helpful for debugging issues on the system.

# Clear the authentication log
echo "" > /var/log/auth.log
echo "Cleared authentication log"

# The authentication log (/var/log/auth.log) tracks authentication attempts, including successful and unsuccessful logins. This log can be useful for identifying attempts to gain unauthorized access to the system.

# Clear the security log
echo "" > /var/log/security
echo "Cleared security log"

# The security log (/var/log/security) tracks security-related events on the system, including firewall activity, failed login attempts, and more. This log can be helpful for identifying potential security issues on the system.

# Clear the Apache access log
echo "" > /var/log/apache2/access.log
echo "Cleared Apache access log"

# The Apache access log (/var/log/apache2/access.log) tracks HTTP requests made to the Apache web server running on the system. This log can be useful for identifying traffic to the server and potential attacks.

# Clear the Apache error log
echo "" > /var


truncate -s 0 /var/log/lastlog
echo "Size of /var/log/lastlog after clearing: $(du -h /var/log/lastlog)"
# The lastlog file contains information about the last time each user logged in.

truncate -s 0 /var/log/btmp
echo "Size of /var/log/btmp after clearing: $(du -h /var/log/btmp)"
# The btmp file tracks failed login attempts, and can reveal attempts to gain unauthorized access to the system.
