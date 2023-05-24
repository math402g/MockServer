import time
import jsonpickle

from paho.mqtt.client import Client, MQTTMessage, Properties, MQTTv5
from paho.mqtt.packettypes import PacketTypes
from JsonEnumHandler import JsonEnumHandler

from models.AntennasPosition import AntennaPosition
from models.DefaultResponse import DefaultResponse
from models.PathSettings import PathSettings
from models.RobotLightIntensity import RobotLightIntensity
from models.RobotMode import RobotMode, RobotModes
from models.RouterSettings import EthernetMode, RouterSettings, SetRouterSettings
from models.SoundFiles import SoundFile, SoundFiles
from models.UltraSoundMode import UltraSoundMode
from models.Diagnostic import Diagnostic
from models.UltraSoundResponse import UltraSoundResponse
from  models.CoreModule import CoreModule

antennaPosition = AntennaPosition.default()
pathSettings = PathSettings.default()
robotLightIntensity = RobotLightIntensity.default()
robotMode = RobotMode.default()
routerSettings = RouterSettings.default()
soundFiles = SoundFiles.default()
ultraSoundMode = UltraSoundMode.default()

updated: bool = False


def load():
    global antennaPosition
    global pathSettings
    global robotLightIntensity
    global robotMode
    global routerSettings
    global soundFiles
    global ultraSoundMode

    antennaPosition = getJsonOrDefault("json/antennaPosition.json", antennaPosition)
    pathSettings = getJsonOrDefault("json/pathSettings.json", pathSettings)
    robotLightIntensity = getJsonOrDefault("json/robotLightIntensity.json", robotLightIntensity)
    robotMode = getJsonOrDefault("json/robotMode.json", robotMode)
    routerSettings = getJsonOrDefault("json/routerSettings.json", routerSettings)
    soundFiles = getJsonOrDefault("json/soundFiles.json", soundFiles)
    ultraSoundMode = getJsonOrDefault("json/ultraSoundMode.json", ultraSoundMode)


def getJsonOrDefault(file_path: str, obj):
    try:
        with open(file_path, "r") as f:
            return jsonpickle.decode(f.read())
    except Exception as e:
        print("error;  {e}".format(e=e))
        with open(file_path, "w") as f:
            f.write(jsonpickle.encode(obj, unpicklable=False))
            return obj


def connect_mqtt():
    client = Client("mqtt5_client", protocol=MQTTv5)
    # client.username_pw_set(username, password)
    client.connect("localhost", 1883)
    return client


def refresh(client: Client):
    global updated

    if updated == False:
        return

    publish_properties = Properties(PacketTypes.PUBLISH)
    publish_properties.UserProperty = ("Content-Type", "application/json")
    publish_properties.UserProperty = ("content-encoding", "UTF-8")

    client.publish("capra/service/tier1/sensors/gnss/antennas/position", jsonpickle.encode(antennaPosition, unpicklable=False), properties=publish_properties)
    client.publish("capra/robot/navigation/path_settings", jsonpickle.encode(pathSettings, unpicklable=False), properties=publish_properties)
    client.publish("capra/robot/light_intensity", jsonpickle.encode(robotLightIntensity, unpicklable=False), properties=publish_properties)
    client.publish("capra/robot/mode", jsonpickle.encode(robotMode, unpicklable=False), properties=publish_properties)
    client.publish("capra/robot/router_settings", jsonpickle.encode(routerSettings, unpicklable=False), properties=publish_properties)
    client.publish("capra/robot/sound_files", jsonpickle.encode(soundFiles, unpicklable=False), properties=publish_properties)
    client.publish("capra/service/tier0/sensors/ultrasound/mode", jsonpickle.encode(ultraSoundMode, unpicklable=False), properties=publish_properties)

    updated = False


def publishTopics(client: Client):
    global updated
    updated = True
    refresh(client)

    while True:
        time.sleep(10)
        diagnostic = Diagnostic.createMock()
        client.publish("capra/robot/diagnostics/core", jsonpickle.encode(diagnostic, unpicklable=False))

        core = CoreModule.createMock()
        client.publish("capra/robot/status/core", jsonpickle.encode(core, unpicklable=False))




def on_connect(client: Client, userData, flags, rc, props):
    if not flags["session present"]:
        client.subscribe("capra/#")


def sendDefaultResponse(client: Client, topic: str, path: str, payload: str, obj):
    global updated
    try:
        obj = jsonpickle.decode(payload)
        with open(path, "w") as f:
            f.write(payload)

        client.publish("{topic}/response".format(topic=topic), jsonpickle.encode(DefaultResponse(True, ""), unpicklable=False), qos=1)
        updated = True
    except Exception as e:
        client.publish("{topic}/response".format(topic=topic), jsonpickle.encode(DefaultResponse(True, e), unpicklable=False), qos=1)
    return obj


def on_set_message(client: Client, userData, msg: MQTTMessage):
    global antennaPosition
    global pathSettings
    global robotLightIntensity
    global robotMode
    global routerSettings
    global soundFiles
    global ultraSoundMode

    global updated

    match msg.topic:
        case "capra/service/tier1/sensors/gnss/antennas/set_position":
            antennaPosition = sendDefaultResponse( client, "capra/service/tier1/sensors/gnss/antennas/set_position","json/antennaPosition.json",  msg.payload.decode(), antennaPosition)
        case "capra/robot/navigation/set_path_settings":
            pathSettings = sendDefaultResponse(client, "capra/robot/navigation/set_path_settings", "json/pathSettings.json", msg.payload.decode(), pathSettings)
        case "capra/robot/set_light_intensity":
            robotLightIntensity = sendDefaultResponse( client,"capra/robot/set_light_intensity", "json/robotLightIntensity.json", msg.payload.decode(), robotLightIntensity,)
        case "capra/robot/set_mode":
            robotMode = sendDefaultResponse(client, "capra/robot/set_mode", "json/robotMode.json", msg.payload.decode(), robotMode)
        case "capra/robot/set_router_settings":
            try:
                setRouterSettings: SetRouterSettings = jsonpickle.decode(msg.payload.decode())
                routerSettings = RouterSettings(EthernetMode[setRouterSettings["set_mode"]])

                with open("json/routerSettings.json", "w") as f:
                    f.write(jsonpickle.encode(routerSettings))

                client.publish("capra/robot/set_router_settings/response", jsonpickle.encode(DefaultResponse(True, ""), unpicklable=False), qos=1)
                updated = True
            except Exception as e:
                client.publish( "capra/robot/set_router_settings/response", jsonpickle.encode(DefaultResponse(False, e), unpicklable=False), qos=1)
        case "capra/service/tier0/sensors/ultrasound/set_mode":
            try:
                obj = jsonpickle.decode(msg.payload.decode())

                with open("json/ultraSoundMode.json", "w") as f:
                    f.write(msg.payload.decode())

                client.publish("capra/service/tier0/sensors/ultrasound/set_mode/response",jsonpickle.encode(UltraSoundResponse(True, obj["mode"], "", 0), unpicklable=False), qos=1)
                updated = True
            except Exception as e:
                client.publish("capra/service/tier0/sensors/ultrasound/set_mode/response", jsonpickle.encode(UltraSoundResponse(False, 0, e, 404), unpicklable=False),qos=1)
        case "capra/robot/upload_sound":
            try:
                soundFile = jsonpickle.decode(msg.payload.decode())
                if soundFile['name'] in map(lambda s: s["name"], soundFiles["sound_files"]): raise Exception("sound file with this name already exist")
                soundFiles["sound_files"].append(soundFile)

                with open("json/soundFiles.json", "w") as f:
                    f.write(jsonpickle.encode(soundFiles))

                client.publish("capra/robot/upload_sound/response", jsonpickle.encode(DefaultResponse(True, ""), unpicklable=False), qos=1)
                updated = True
            except Exception as e:
                client.publish("capra/robot/upload_sound/response",jsonpickle.encode(DefaultResponse(False, e.args[0]), unpicklable=False), qos=1)
    refresh(client)


def run():
    jsonpickle.handlers.registry.register(EthernetMode, JsonEnumHandler)
    jsonpickle.handlers.registry.register(RobotModes, JsonEnumHandler)

    load()
    client = connect_mqtt()
    client.loop_start()
    client.on_connect = on_connect
    client.message_callback_add("capra/robot/navigation/set_path_settings", on_set_message)
    client.message_callback_add("capra/service/tier1/sensors/gnss/antennas/set_position", on_set_message)
    client.message_callback_add("capra/robot/set_light_intensity", on_set_message)
    client.message_callback_add("capra/robot/set_mode", on_set_message)
    client.message_callback_add("capra/robot/set_router_settings", on_set_message)
    client.message_callback_add("capra/service/tier0/sensors/ultrasound/set_mode", on_set_message)
    client.message_callback_add("capra/robot/upload_sound", on_set_message)
    publishTopics(client)


if __name__ == "__main__":
    run()
