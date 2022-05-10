#!/bin/bash

py3="no"
#Check for python3
echo "Checking for python3..."
type -P python3 >/dev/null 2>&1 && py3="yes"
if [ "$py3" -eq "yes" ]; then
  echo "Python3 installed, continuing..."
else
  echo "Python3 not installed trying to install..."
  sudo apt install python3 || echo "Unable to install python3 from apt, manualy install python3 then run this script again."
  exit 1
fi
echo "Installing GUI dependencies..."
#Install python packages
sudo pip3 install -r packages.txt || echo "failed to install required packages"
