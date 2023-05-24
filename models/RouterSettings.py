from enum import Enum


class EthernetMode(Enum):
    WAN = 0
    LAN = 1


class SetRouterSettings:
    def __init__(self, password: str, set_mode: EthernetMode):
        self.password = password
        self.set_mode = set_mode

class RouterSettings: 
    def __init__(self, mode: EthernetMode):
        self.mode = mode
    
    def default():
        return RouterSettings(EthernetMode.WAN)



