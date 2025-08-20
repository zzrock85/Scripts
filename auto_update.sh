#!/bin/bash
# This script performs an automatic update of the system and logs the output.

LOGFILE="/var/log/update.log"

echo "Automatic update" | tee "$LOGFILE"
date >> "$LOGFILE"
echo "apt update" | tee -a "$LOGFILE"
apt update >> "$LOGFILE" 2>&1
echo "Checking for available updates..." | tee -a "$LOGFILE"
UPDATES=$(apt list --upgradable 2>/dev/null | grep -v "Listing..." | wc -l)
if [ "$UPDATES" -eq 0 ]; then
    echo "No updates available. Exiting." | tee -a "$LOGFILE"
    exit 0
fi
echo "apt upgrade" | tee -a "$LOGFILE"
apt upgrade -y >> "$LOGFILE" 2>&1
echo "apt autoremove" | tee -a "$LOGFILE"
apt autoremove -y >> "$LOGFILE" 2>&1
echo "Script execution completed successfully." | tee -a "$LOGFILE"
if [ -f /var/run/reboot-required ]; then
    echo "Reboot required. Rebooting now." | tee -a "$LOGFILE"
    reboot
else
    echo "No reboot required." | tee -a "$LOGFILE"
fi