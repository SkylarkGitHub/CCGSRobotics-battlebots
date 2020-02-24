#!/usr/bin/bash
cd CCGSRobotics-battlebots/
lxterminal -e sudo motion &
lxterminal -e python3 robot.py &
sudo node index.js
