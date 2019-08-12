import json
from flask import Flask
from switchmate import *

app = Flask(__name__)


@app.route("/device/on/<macaddress>", methods=['GET'])
def device_on(macaddress):
    return macaddress + " is on"


@app.route("/device/off/<macaddress>", methods=['GET'])
def device_off(macaddress):
    return macaddress + " is off"


@app.route("/devices", methods=['GET'])
def devices():
    switchmates = scan(
        'Scanning...',
        success_msg='Found Switchmates:',
        timeout=30,
        process_entry=lambda switchmate: print(switchmate.addr),
    )
    return json.dumps(switchmates)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
