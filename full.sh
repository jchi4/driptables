#!/bin/bash  
#Bash script to run prerequisite commands and to wget driptables
sudo apt update -y  
sudo apt-get install python3.9 -y  
sudo apt-get install iptables-persistent netfilter-persistent
wget https://github.com/jchi4/driptables/raw/main/driptables.py