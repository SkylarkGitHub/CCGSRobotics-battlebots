from servo import *

class Robot:
    def __init__(self, n, servolist):
        self.name = n
        self.servos = servolist


battlebotServos = [
    Servo("front_left_wheel", 3, "wheel", ax12a),
    Servo("front_right_wheel", 2, "wheel", ax12a),
    Servo("back_left_wheel", 4, "wheel", ax12a),
    Servo("back_right_wheel", 1, "wheel", ax12a)
]

battlebot = Robot("battlebot", battlebotServos)

emubotServos = [
    Servo("front_left_wheel", 3, "wheel", ax12a),
    Servo("front_right_wheel", 2, "wheel", ax12a),
    Servo("back_left_wheel", 4, "wheel", ax12a),
    Servo("back_right_wheel", 1, "wheel", ax12a),
    Servo("shoulder_joint", 5, "joint", ax12a),
    Servo("elbow_joint", 6, "joint", ax12a),
    Servo("wrist_joint", 7, "joint", ax12a)
]

emubot = Robot("emubot", emubotServos)