from servo import *

class Robot:
    def __init__(self, n, servolist):
        self.name = n
        self.servos = servolist


battlebotServos = [
    new Servo("front_left_wheel", 3, "wheel", ax12a),
    new Servo("front_right_wheel", 2, "wheel", ax12a),
    new Servo("back_left_wheel", 4, "wheel", ax12a),
    new Servo("back_right_wheel", 1, "wheel", ax12a)
]

battlebot = new Robot("battlebot", battlebotServos)

emubotServos = [
    new Servo("front_left_wheel", 3, "wheel", ax12a),
    new Servo("front_right_wheel", 2, "wheel", ax12a),
    new Servo("back_left_wheel", 4, "wheel", ax12a),
    new Servo("back_right_wheel", 1, "wheel", ax12a),
    new Servo("shoulder_joint", 5, "joint", ax12a),
    new Servo("elbow_joint", 6, "joint", ax12a),
    new Servo("wrist_joint", 7, "joint", ax12a)
]

emubot = new Robot("emubot", emubotServos)