import json
from uniboard_raspberrypi import UniboardRaspberryPi

data = json.dumps({'temp': 21.2, 'humidity': 29.8})

piClient = UniboardRaspberryPi('25f6db34-9ff1-47f4-b7bb-3721cafb2e23')

# return http.client.HTTPResponse object
piClient.http('https://uniboard.io/data_api/device/59db5cd3d6021211cb346b0b', data)


def on_mqtt_connect(client, userdata, flags, rc):
    piClient.mqtt('/data_api/device/59db5cd3d6021211cb346b0b', data)

piClient.on_mqtt_connect = on_mqtt_connect
piClient.connect_mqtt()
