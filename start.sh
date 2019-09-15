#!/usr/bin/bash
lxterminal -e sudo motion &
lxterminal -e python3 robot.py &
sudo node index.js