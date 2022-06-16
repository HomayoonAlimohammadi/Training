from iot.device import Device
from iot.devices import Curtain


def handle_device(device: Device):
    device.connect()
    device.say_hello()
    device.disconnect()

def main():
    device = Curtain()
    handle_device(device)


if __name__ == '__main__':
    main()