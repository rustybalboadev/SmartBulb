import requests, json, os.path

class STAPI():
    def __init__(self):
        configPath = os.path.dirname(__file__) + "/../config.json"
        f = open(configPath, "r")
        data = json.load(f)
        self.headers = {
            "Authorization": "Bearer " + data["apikey"],
            "Content-Type": "application/json"
        }
        self.endpoint = "https://api.smartthings.com/v1/"
        self.deviceID = data["deviceID"]

    def changeColor(self, hue: int, level: int, saturation: int):
        payload = {
            "commands": [
                {
                    "capability": "colorControl",
                    "command": "setColor",
                    "arguments": [
                        {
                            "hue": hue,
                            "level": level,
                            "saturation": saturation
                        }
                    ]
                }
            ]
        }
        req = requests.post(self.endpoint + "devices/{}/commands".format(self.deviceID), headers=self.headers, data=json.dumps(payload))

    def changeDim(self, level):
        payload = {
            "commands": [
                {
                    "capability": "switchLevel",
                    "command": "setLevel",
                    "arguments": [100]
                }
            ]
        }
        req = requests.post(self.endpoint + "devices/{}/commands".format(self.deviceID), headers=self.headers, data=json.dumps(payload))

    @staticmethod
    def adjustHueBase(hue):
        return (hue/365) * 100