from functions import *

def send_robot_commands(ROBOT, baseSpeed, baseAngle)
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
