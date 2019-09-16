from simple_websocket_server import WebSocketServer, WebSocket
from functions import *
import math

# The robot is setup as a battlebot, with the wheels in their respective positions.
robot = {
    "name": "battlebot",
    "front_left_wheel": 3,
    "front_right_wheel": 2,
    "back_left_wheel": 4,
    "back_right_wheel": 1,
}

# if the robot is named "battlebot", the wheels are setup using the wheelMode("servo id") function.
if robot["name"] == "battlebot":
    wheelMode(robot["front_left_wheel"])
    wheelMode(robot["front_right_wheel"])
    wheelMode(robot["back_left_wheel"])
    wheelMode(robot["back_right_wheel"])

class RobotServer(WebSocket):
    def handle(self):
        # a try statement is used to prevent a data processing error from crashing the program.
        try:
            # The baseSpeed and baseAngle are read from the incoming packet from the websocket client.
            baseSpeed, baseAngle = map(int, self.data.split("|"))

            if robot["name"] == "battlebot":
                # If the VirtualJoystick is below the y-axis, it changes the speed to a negative, indictaing a backwards direction.
                if baseAngle < 0:
                    baseSpeed = baseSpeed * -1
                    baseAngle = abs(baseAngle)

                # Uses the angle of the joystick to calculate the "true" speeds of the wheels.
                # math.sin(baseAngle) is used to calculate the speed of the slower wheel.

                if baseAngle < 90: # The joystick is to the right of the y-axis
                    leftWheelSpeed = baseSpeed
                    rightWheelSpeed = int(baseSpeed * abs(math.sin((baseAngle*math.pi)/180)))

                elif baseAngle > 90: # The joystick is to the left of the y-axis
                    rightWheelSpeed = baseSpeed
                    leftWheelSpeed = int(baseSpeed * abs(math.sin((baseAngle*math.pi)/180)))

                else: # The joystick is along the y-axis.
                    rightWheelSpeed = baseSpeed
                    leftWheelSpeed = baseSpeed 

                # Since the servos are set to spin the same direction, the left wheels are set to spin backwards to maintain the 
                # direction of the robot, as the servos on one side are flipped.
                rightWheelSpeed *= -1

                # Moves the four wheels according to the new, calculated speeds.
                moveWheel(robot["front_left_wheel"], leftWheelSpeed)
                moveWheel(robot["back_left_wheel"], leftWheelSpeed)

                moveWheel(robot["front_right_wheel"], rightWheelSpeed)
                moveWheel(robot["back_right_wheel"], rightWheelSpeed)

                # Print() statement added for debugging purposes. Comment print statement when not debugging, since it will 
                # significantly decrease performance, making the operation of the robot rather difficult. 
                # print(leftWheelSpeed, rightWheelSpeed)
            
        # Except statement will print out the error, preventing the program from crashing 
        # whilst still providing infomation for debuggings purposes.
        except Exception as e:
            print(e)

    # The following two functions (connected(self) & handle_close(self)) are used to indicate the connections of clients to the websocket.
    def connected(self):
        print('Client', self.address, 'Connected.')

    def handle_close(self):
        print('Client', self.address, 'Closed.')

# The websocket server is setup on port 9999 on the default address, in this case "192.168.100.1"
server = WebSocketServer('', 9999, RobotServer)
server.serve_forever()