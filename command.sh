#!/bin/bash

# Update package lists
apt update && apt upgrade

# Install necessary packages
# Use pkg install -y for non-critical packages
pkg install -y x11-repo git python-pip vim clang nmap tsu

# Prompt user for confirmation before installing root-repo (if needed)
read -p "Do you want to install root-repo (grants broader access, use with caution)? [y/N] " response
if [[ "$response" =~ ^[Yy]$ ]]; then
  pkg install root-repo
fi

# Grant storage access (cautiously consider alternatives)
termux-setup-storage

# Git clone termux-sudo (avoid direct file system modification)
git clone https://gitlab.com/st42/termux-sudo

# Build and install termux-sudo within the cloned directory (safer approach)
cd termux-sudo
./build.sh

# Return to the original directory
cd ..

# Create a test directory (modify path if needed)
mkdir -p storage/shared/test && cd storage/shared/test

# Clone PPPwn with submodules
git clone --recursive https://github.com/TheOfficialFloW/PPPwn

# Install requirements using pip within the cloned directory
cd PPPwn
pip install -r requirements.txt

# Note: Avoid mixing `sudo pip` and `pip` in the same script for security reasons

# Additional notes:
# - Consider using a virtual environment for managing project dependencies.
# - Explore alternative approaches to granting storage access if `termux-setup-storage` is not necessary.

echo "Script execution complete!"
