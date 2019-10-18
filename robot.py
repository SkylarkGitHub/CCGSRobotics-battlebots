from simple_websocket_server import WebSocketServer, WebSocket
from functions import *
from robot_commands import *
import math

# The robot is setup as a battlebot, with the wheels in their respective positions.
robot = {
    "name": "emobot",
    "front_left_wheel": 1,
    "front_right_wheel": 2,
    "back_left_wheel": 3,
    "back_right_wheel": 4,
    "shoulder": 5,
    "wrist": 6,
    "camera_pan": 7
}

# if the robot is named "battlebot", the wheels are setup using the wheelMode("servo id") function.
if robot["name"] == "battlebot":
    wheelMode(robot["front_left_wheel"])
    wheelMode(robot["front_right_wheel"])
    wheelMode(robot["back_left_wheel"])
    wheelMode(robot["back_right_wheel"])

elif robot["name"] == "emobot":
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
            
            command_robot(robot, baseSpeed, baseAngle)
            
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
