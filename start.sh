#!/usr/bin/bash
sudo pkill python
cd CCGSRobotics-battlebots/
python3 robot.py &
sudo node index.js
