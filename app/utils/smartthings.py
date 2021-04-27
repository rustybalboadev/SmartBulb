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

    def grabCurrent(self):
        req = requests.get(self.endpoint + "devices/{}/status".format(self.deviceID), headers=self.headers).json()
        hue = req["components"]["main"]["colorControl"]["hue"]["value"]
        sat = req["components"]["main"]["colorControl"]["saturation"]["value"]
        hue = (hue/100) * 365
        return hue, sat, 100

    @staticmethod
    def adjustHueBase(hue):
        return (hue/365) * 100