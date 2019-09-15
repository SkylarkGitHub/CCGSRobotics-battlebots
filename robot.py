from simple_websocket_server import WebSocketServer, WebSocket
from functions import *
import math

robot = {
    "name": "battlebot",
    "front_left_wheel": 1,
    "front_right_wheel": 3,
    "back_left_wheel": 2,
    "back_right_wheel": 4,
}

if robot["name"] == "battlebot":
    wheelMode(robot["front_left_wheel"])
    wheelMode(robot["front_right_wheel"])
    wheelMode(robot["back_left_wheel"])
    wheelMode(robot["back_right_wheel"])

class RobotServer(WebSocket):
    def handle(self):
        try:
            baseSpeed, baseAngle = map(int, self.data.split("|"))
            if robot["name"] == "battlebot":
                # Converts negative angles into positive angles, and sets the base speed to be backwards
                if baseAngle < 0:
                    baseSpeed = int(baseSpeed * -1)
                    baseAngle = int(abs(baseAngle))

                # Uses the angle of the joystick to calculate the "true" speeds of the wheels.
                if baseAngle > 90:
                    leftWheelSpeed = int(baseSpeed * abs(math.sin(baseAngle))))
                    rightWheelSpeed = baseSpeed

                elif baseAngle < 90:
                    rightWheelSpeed = int(baseSpeed * abs(math.sin(baseAngle)))
                    leftWheelSpeed = baseSpeed

                else:
                    rightWheelSpeed = int(baseSpeed * abs(math.sin(baseAngle)))
                    leftWheelSpeed = baseSpeed

                # Moves the wheels according to the calculated speed.
                moveWheel(robot["front_left_wheel"], leftWheelSpeed)
                moveWheel(robot["back_left_wheel"], leftWheelSpeed)

                moveWheel(robot["front_left_wheel"], rightWheelSpeed)
                moveWheel(robot["back_left_wheel"], rightWheelSpeed)

            #print(baseSpeed,baseAngle)

        except Exception as e:
            print(e)

    def connected(self):
        print(self.address, 'connected')

    def handle_close(self):
        print(self.address, 'closed')

server = WebSocketServer('', 9999, RobotServer)
server.serve_forever()