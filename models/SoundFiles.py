from ast import List


class SoundFile:
    def __init__(self, name:str, sound_file:str):
        self.name = name
        self.sound_file = sound_file

class SoundFiles:
    def __init__(self, sound_files: List):
        self.sound_files = sound_files

    def default():
        return SoundFiles([])
