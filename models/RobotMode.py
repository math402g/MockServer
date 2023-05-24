from enum import Enum


class RobotModes(Enum):
    INDOOR = 0
    OUTDOOR = 1
    BOTH = 2


class RobotMode:
    def __init__(self, robot_mode: RobotModes):
        self.robot_mode = robot_mode

    def default():
        return RobotMode(RobotModes.BOTH)
