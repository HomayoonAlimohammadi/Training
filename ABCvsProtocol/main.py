from iot.client import handle_device
from iot.devices import Curtain


device = Curtain()
handle_device(device)