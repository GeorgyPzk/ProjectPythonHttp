#!/bin/bash
sudo apt update -y
sudo apt install python-pip -y
sudo pip install requests
sudo pip install mysql-connector-python
sudo python ./task-post.py