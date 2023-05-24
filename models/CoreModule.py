import random

class CoreModule:
    def __init__(self, battery_percentage: int):
        self.battery_percentage = battery_percentage


    def createMock():
        return CoreModule(battery_percentage= random.randint(0, 100))