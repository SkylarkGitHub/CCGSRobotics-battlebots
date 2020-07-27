from pyax12.connection import Connection
servo_connection = Connection(port="/dev/ttyACM0", baudrate=1000000)

servo_connection.flush()

def scaleValues(self, val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.
    """
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

class ServoModel:
    def __init__(self, modelName, cw_angle_limit, ccw_angle_limit):
        self.modelName = modelName
        self.cw_angle_limit = cw_angle_limit
        self.ccw_angle_limit = ccw_angle_limit


class Servo:
    def __init__(self, n, ID, t, m):
        self.name = n
        self.ID = ID
        self.type = t
        self.model = m

    # === JOINT FUNCTIONS === #

    # Set up a dynamixel so that it behaves like joint.
    def jointMode(self):
            servo_connection.set_cw_angle_limit(self.ID,self.model.cw_angle_limit,False)
            servo_connection.set_ccw_angle_limit(self.ID,self.model.ccw_angle_limit,False)

    # Move a dynamixel that has been set up as a joint.
    def moveJoint(self, position):
            mappedPosition = scaleValues(position, [0, 100], [self.model.cw_angle_limit, self.model.ccw_angle_limit])
            servo_connection.goto(int(self.ID), int(mappedPosition), 100, False)

    # === WHEEL FUNCTIONS === #

    # Set up a dynamixel so that it behaves like wheel.
    def wheelMode(self):
            servo_connection.set_ccw_angle_limit(self.ID,0,False)
            servo_connection.set_cw_angle_limit(self.ID,0,False)

    # Move a dynamixel that has been set up as a wheel.
    def moveWheel(self, speed):
            mappedSpeed = scaleValues(speed, [-100, 100], 0, 2047)
                    
            servo_connection.flush()
            servo_connection.goto(int(self.ID), 0, int(mappedSpeed), degrees=False)

        
ax12a = ServoModel("ax-12a", 0, 1023)
ax18a = ServoModel("ax-18a", 0, 1023)