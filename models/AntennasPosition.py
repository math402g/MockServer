class Point:
    def __init__(self, x:float, y:float, z:float):
        self.x = x
        self.y = y
        self.z = z

class Quaternion:
    def __init__(self, x:float, y:float, z:float, w:float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

class Pose:
    def __init__(self, point:Point, quaternion:Quaternion):
        self.point = point
        self.quaternion = quaternion

class AntennaPosition:
    def __init__(self, rover_pose: Pose, base_pose: Pose):
        self.rover_pose =rover_pose 
        self.base_pose = base_pose

    def default():
        return AntennaPosition(Pose(Point(0,0,0), Quaternion(0,0,0,0)), Pose(Point(0,0,0), Quaternion(0,0,0,0)))