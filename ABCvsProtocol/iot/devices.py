from iot.device import Device

class Lamp(Device):

    def connect(self):
        print('Connecting Lamp...')

    def disconnect(self):
        print('Disconnecting Lamp')

    def say_hello(self):
        print('Hello from Lamp!')


class Curtain(Device):

    def connect(self):
        print('Connecting Curtains...')

    def disconnect(self):
        print('Disconnecting Curtains')

    def say_hello(self):
        print('Hello from Curtains!')