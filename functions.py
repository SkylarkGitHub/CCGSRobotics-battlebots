from pyax12.connection import Connection
servo_connection = Connection(port="/dev/ttyACM0", baudrate=1000000)

servo_connection.flush()

# Consult the robotics emanual for more infomation on how 
# the dynamixel servos interpret communications.

# === JOINT FUNCTIONS === #

# Set up a dynamixel so that it behaves like joint.
def jointMode(ID):
        servo_connection.set_cw_angle_limit(ID,0,False)
        servo_connection.set_ccw_angle_limit(ID,1023,False)

# Move a dynamixel that has been set up as a joint.
def moveJoint(ID, position, speed):
        servo_connection.goto(int(ID), int(position), int(speed), False)

# === WHEEL FUNCTIONS === #

# Set up a dynamixel so that it behaves like wheel.
def wheelMode(ID):
        servo_connection.set_ccw_angle_limit(ID,0,False)
        servo_connection.set_cw_angle_limit(ID,0,False)

# Move a dynamixel that has been set up as a wheel.
def moveWheel(ID, speed):
        # Negative speed moves CW, positive speed moves CCW
        # Convert negative values of speed to between 1024 and 2047
        
        speed = (speed) * 1023 / 100

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
                 
        servo_connection.flush()
        servo_connection.goto(int(ID), 0, int(speed), degrees=False)

print('* functions defined *')