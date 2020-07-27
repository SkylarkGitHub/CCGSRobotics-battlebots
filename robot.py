from simple_websocket_server import WebSocketServer, WebSocket
from robot_servo_layouts import *
import math

robot = battlebot

for servo in robot.servos:
    if servo.type == "wheel":
        servo.wheelMode()
    elif servo.type == "joint":
        servo.jointMode()

class RobotServer(WebSocket):
    def handle(self):
        # a try statement is used to prevent a data processing error from crashing the program.
        try:

            if "Joint:" in self.data:
                servoName, changeValue = self.data.split(",").replace("Joint: ")
                print(servoName,changeValue)

            elif "Wheels: " in self.data:
                # The baseSpeed and baseAngle are read from the incoming packet from the websocket client.
                baseSpeed, baseAngle = map(int, self.data.split(",").replace("Wheels: "))

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

                # Since the servos are set to spin the same direction, the right wheels are set to spin backwards to maintain the 
                # direction of the robot, as the servos on one side are flipped over.
                rightWheelSpeed *= -1

                # Moves the four wheels according to the new, calculated speeds.
                for servo in robot.servos:
                    if servo.type == "wheel":
                        if servo.name == "front_left_wheel" or servo.name == "back_left_wheel":
                            servo.moveWheel(leftWheelSpeed)
                        elif servo.name == "front_right_wheel" or servo.name == "back_right_wheel":
                            servo.moveWheel(rightWheelSpeed)
            
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