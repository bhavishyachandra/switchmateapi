import json
from flask import Flask
from switchmate import *

app = Flask(__name__)


@app.route("/device/status/<macaddress>", methods=['GET'])
def device_status(macaddress):
    return status_by_mac(macaddress)


@app.route("/device/on/<macaddress>", methods=['GET'])
def device_on(macaddress):
    switch_by_mac(macaddress, 'on')
    return macaddress + " is on"


@app.route("/device/off/<macaddress>", methods=['GET'])
def device_off(macaddress):
    switch_by_mac(macaddress, 'off')
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
