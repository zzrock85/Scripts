#!/bin/bash

echo "Automatic update" | tee -a update.log
date >> update.log
echo "apt update" | tee -a update.log
apt update >> update.log 2>&1
echo "apt upgrade" | tee -a update.log
apt upgrade -y >> update.log 2>&1
echo "Script execution completed successfully." | tee -a update.log
reboot