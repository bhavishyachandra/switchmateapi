from flask import Flask

app = Flask(__name__)


@app.route("/device/on/<macaddress>", methods=['GET'])
def device_on(macaddress):
    return macaddress + " is on"


@app.route("/device/off/<macaddress>", methods=['GET'])
def device_off(macaddress):
    return macaddress + " is off"


@app.route("/devices", methods=['GET'])
def device_off(macaddress):
    return "list of devices"


if __name__ == '__main__':
    app.run(debug=True)
