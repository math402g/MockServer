from ast import List
import random


class KeyValuePair:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value


class DiagnosticMessage:
    def __init__(
        self,
        level: int,
        name: str,
        message: str,
        hardware_id: int,
        values: List,
    ):
        self.level = level
        self.name = name
        self.message = message
        self.hardware_id = hardware_id
        self.values = values


class Diagnostic:
    def __init__(self, status: List):
        self.status = status

    def createMock():
        return Diagnostic(
            [
                DiagnosticMessage(
                    level=0,
                    name="CONTROL_SYSTEM",
                    message="Control System",
                    hardware_id="",
                    values=[
                        KeyValuePair("SW_VERSION_MAJOR", "0"),
                        KeyValuePair("SW_VERSION_MINOR", "22"),
                        KeyValuePair("SW_VERSION_PATCH", "2"),
                    ],
                ),
                DiagnosticMessage(
                    level=0,
                    name="HAS_FRONT",
                    message="Front Angle Sensor",
                    hardware_id="",
                    values=[
                        KeyValuePair(
                            "MAGNETIC_FIELD", random.randint(500, 899).__str__()
                        ),
                        KeyValuePair("SW_VERSION_MAJOR", "0"),
                        KeyValuePair("SW_VERSION_MINOR", "22"),
                        KeyValuePair("SW_VERSION_PATCH", "2"),
                        KeyValuePair("TEMPERATURE", random.randint(20, 99).__str__()),
                    ],
                ),
                DiagnosticMessage(
                    level=0,
                    name="HAS_REAR",
                    message="Rear Angle Sensor",
                    hardware_id="",
                    values=[
                        KeyValuePair(
                            "MAGNETIC_FIELD", random.randint(500, 899).__str__()
                        ),
                        KeyValuePair("SW_VERSION_MAJOR", "0"),
                        KeyValuePair("SW_VERSION_MINOR", "22"),
                        KeyValuePair("SW_VERSION_PATCH", "2"),
                        KeyValuePair("TEMPERATURE", random.randint(20, 99).__str__()),
                    ],
                ),
                DiagnosticMessage(
                    level=0,
                    name="HMC_FRONT",
                    message="Front Wheel",
                    hardware_id="",
                    values=[
                        KeyValuePair("CURRENT", random.uniform(0.20, 0.40).__str__()),
                        KeyValuePair("HUMIDITY", random.randint(30, 70).__str__()),
                        KeyValuePair("SW_VERSION_MAJOR", "0"),
                        KeyValuePair("SW_VERSION_MINOR", "22"),
                        KeyValuePair("SW_VERSION_PATCH", "2"),
                        KeyValuePair("TEMPERATURE", random.randint(20, 99).__str__()),
                    ],
                ),
                DiagnosticMessage(
                    level=0,
                    name="HMC_LEFT",
                    message="Left Wheel",
                    hardware_id="",
                    values=[
                        KeyValuePair("CURRENT", random.uniform(0.20, 0.40).__str__()),
                        KeyValuePair("HUMIDITY", random.randint(30, 70).__str__()),
                        KeyValuePair("SW_VERSION_MAJOR", "0"),
                        KeyValuePair("SW_VERSION_MINOR", "22"),
                        KeyValuePair("SW_VERSION_PATCH", "2"),
                        KeyValuePair("TEMPERATURE", random.randint(20, 99).__str__()),
                    ],
                ),
                DiagnosticMessage(
                    level=0,
                    name="HMC_REAR",
                    message="Rear Wheel",
                    hardware_id="",
                    values=[
                        KeyValuePair("CURRENT", random.uniform(0.20, 0.40).__str__()),
                        KeyValuePair("HUMIDITY", random.randint(30, 70).__str__()),
                        KeyValuePair("SW_VERSION_MAJOR", "0"),
                        KeyValuePair("SW_VERSION_MINOR", "22"),
                        KeyValuePair("SW_VERSION_PATCH", "2"),
                        KeyValuePair("TEMPERATURE", random.randint(20, 99).__str__()),
                    ],
                ),
                DiagnosticMessage(
                    level=0,
                    name="HMC_RIGHT",
                    message="Right Wheel",
                    hardware_id="",
                    values=[
                        KeyValuePair("CURRENT", random.uniform(0.20, 0.40).__str__()),
                        KeyValuePair("HUMIDITY", random.randint(30, 70).__str__()),
                        KeyValuePair("SW_VERSION_MAJOR", "0"),
                        KeyValuePair("SW_VERSION_MINOR", "22"),
                        KeyValuePair("SW_VERSION_PATCH", "2"),
                        KeyValuePair("TEMPERATURE", random.randint(20, 99).__str__()),
                    ],
                ),
                DiagnosticMessage(
                    level=0,
                    name="HUL_LEFT",
                    message="Left Ultrasound and Brake",
                    hardware_id="",
                    values=[
                        KeyValuePair("SW_VERSION_MAJOR", "0"),
                        KeyValuePair("SW_VERSION_MINOR", "6"),
                        KeyValuePair("SW_VERSION_PATCH", "1"),
                    ],
                ),
                DiagnosticMessage(
                    level=0,
                    name="HUL_RIGHT",
                    message="Right Ultrasound and Brake",
                    hardware_id="",
                    values=[
                        KeyValuePair("SW_VERSION_MAJOR", "0"),
                        KeyValuePair("SW_VERSION_MINOR", "6"),
                        KeyValuePair("SW_VERSION_PATCH", "1"),
                    ],
                ),
                 DiagnosticMessage(
                    level=0,
                    name="POWER_SYSTEM",
                    message="Power System",
                    hardware_id="",
                    values=[
                        KeyValuePair("HUMIDITY", random.randint(30, 70).__str__()),
                        KeyValuePair("SW_VERSION_MAJOR", "0"),
                        KeyValuePair("SW_VERSION_MINOR", "8"),
                        KeyValuePair("SW_VERSION_PATCH", "2"),
                        KeyValuePair("TEMPERATURE", random.randint(20, 99).__str__()),
                    ],
                ),
            ]
        )
