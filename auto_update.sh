#!/bin/bash
# This script performs an automatic update of the system and logs the output.

LOGFILE="/var/log/update.log"

echo "Automatic update" | tee "$LOGFILE"
date >> "$LOGFILE"
echo "apt update" | tee -a "$LOGFILE"
apt update >> "$LOGFILE" 2>&1
echo "apt upgrade" | tee -a "$LOGFILE"
apt upgrade -y >> "$LOGFILE" 2>&1
echo "apt autoremove" | tee -a "$LOGFILE"
apt autoremove -y >> "$LOGFILE" 2>&1
echo "Script execution completed successfully." | tee -a "$LOGFILE"
reboot
