#!/usr/bin/bash
sudo apt-get update
sudo apt-get install node.js
sudo apt-get install npm
npm install express
sudo -H pip3 install simple-websocket-server
sudo -H pip3 install pyax12
git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
sudo ./RPi_Cam_Web_Interface/install.sh