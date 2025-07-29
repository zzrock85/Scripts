#!/bin/bash


if [ "$(id -u)" -ne 0 ]; then
    echo "Git configuration"
    git config --global user.name "Name"
    git config --global user.email "email@test.com"
    echo "Generating an SSH key"
    ssh-keygen -o -t rsa -C “email@test.com”
    echo "Configuration complete, run the script again as root."
    exit 1
else
    echo "Running script as root..."
    echo "apt update"
    apt update

    echo "apt upgrade"
    apt upgrade -y

    echo "apt install mc nmon"
    apt install mc nmon -y

    echo "Script execution completed successfully."
    echo "Execute the 'reboot' command to restart the system."
    exit 0
fi
