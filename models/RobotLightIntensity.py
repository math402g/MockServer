class RobotLightIntensity:
    def __init__(self, intensity:int):
        self.intensity = intensity
    
    def default():
        return RobotLightIntensity(0)