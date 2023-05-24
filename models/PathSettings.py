class PathSettings:
    def __init__(self, max_point_deviation:float, turning_radius: float, offset_range:float):
        self.max_point_deviation = max_point_deviation
        self.turning_radius = turning_radius
        self.offset_range = offset_range
    
    def default():
        return PathSettings(0,0,0)