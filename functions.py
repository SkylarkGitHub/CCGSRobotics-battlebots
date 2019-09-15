from pyax12.connection import Connection
import time
import threading
sc = Connection(port="/dev/ttyACM0", baudrate=1000000)

sc.flush()

# === JOINTS === #

# Set up a dynamixel so that it behaves like joint
def jointMode(ID):
        sc.set_cw_angle_limit(ID,0,False)
        sc.set_ccw_angle_limit(ID,1023,False)

# Move a dynamixel that has been set up as a joint
def moveJoint(ID, position, speed):
        #print(ID,position,speed)
        sc.goto(int(ID), int(position), int(speed), False)

# === WHEELS === #

# Set up a dynamixel so that it behaves like wheel
def wheelMode(ID):
        sc.set_ccw_angle_limit(ID,0,False)
        sc.set_cw_angle_limit(ID,0,False)

# Move a dynamixel that has been set up as a wheel

def moveWheel(ID, speed):
        # Negative speed moves CW, positive speed moves CCW
        # Convert negative values of speed to between 1024 and 2047

        speed = speed * 1023 / 100

        if speed < 0:
                # Limit allowed reverse speed to prevent errors
                if speed < -1024:
                        speed = 2047
                else:
                        speed = 1023 - speed
                
        else:
                if speed > 1023:
                        # Limit allowed forward speed to prevent errors
                        speed = 1023
                 
        sc.flush()
        sc.goto(int(ID), 0, int(speed), degrees=False)

print('* functions defined *')