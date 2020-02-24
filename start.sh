#!/usr/bin/bash
cd CCGSRobotics-battlebots/
sudo motion &
python3 robot.py &
sudo node index.js
