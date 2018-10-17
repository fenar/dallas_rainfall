#!/bin/bash
# Author: Fatih E. NAR
# This step for the users of Ubuntu VM as their Jump-Host
sudo apt-get update && sudo apt-get -y upgrade
sudo apt-get install python-pip -y
pip install -r requirements.txt -t lib
