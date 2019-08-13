Instructions to install:

```console
curl https://raw.githubusercontent.com/bhavishyachandra/switchmateapi/master/run.sh -o run.sh
chmod u+x run.sh
./run.sh
```

Instructions to use:
GET <ipaddress>/devices - list of all switchmates
GET <ipaddress>/device/on/<macaddress> - turns on the switchmate
GET <ipaddress>/device/off/<macaddress> - turns off the switchmate
GET <ipaddress>/device/status/<macaddress> - returns 1 if on, 0 if off

Known limitations:
only works on Switchmates that do not require auth token. (firmware > 2.9.15)

Tested on Raspberry Pi 3 with a generic usb bluetooth dongle
