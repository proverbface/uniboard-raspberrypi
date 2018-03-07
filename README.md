# uniboard-raspberrypi
`uniboard_raspberrypi` is a [Uniboard](https://uniboard.io) client module for [Raspberry Pi](https://www.raspberrypi.org) device.
With `uniboard_raspberrypi`, sending data to Uniboard system through HTTP(S) or MQTT protocol would be pretty easy and simple.

## Installation
```sh
$ pip3 install uniboard_raspberrypi
```

## Usage
Import `uniboard_raspberrypi` module and create a client object:
```python
from uniboard_raspberrypi import UniboardRaspberryPi

# Pass token when creating client object. The token is used for client authentication and can be found in Uniboard's Settings tab.
piClient = UniboardRaspberryPi('25f6db34-9ff1-47f4-b7bb-3721cafb2e23')

# If the device does not need authentication, just omit the token.
piClient = UniboardRaspberryPi()
```

Send data through HTTP(S) protocol:
```python
# clientObject.http(<deviceURL>, <dataString>);
# return http.client.HTTPResponse object
data = json.dumps({'temp': 21.2, 'humidity': 29.8})
piClient.http('https://uniboard.io/data_api/device/59db5cd3d6021211cb346b0b', data)
```

Send data through MQTT protocol:
```python
# clientObject.connect_mqtt();
# clientObject.mqtt(<deviceTopic>, <dataString>);
data = json.dumps({'temp': 21.2, 'humidity': 29.8})

def on_mqtt_connect(client, userdata, flags, rc):
    piClient.mqtt('/data_api/device/59db5cd3d6021211cb346b0b', data)

piClient.on_mqtt_connect = on_mqtt_connect
piClient.connect_mqtt()
```

## License
(The MIT License)

Copyright (c) 2017-2018 Chuan Shao &lt;shaochuancs@gmail.com&gt;
