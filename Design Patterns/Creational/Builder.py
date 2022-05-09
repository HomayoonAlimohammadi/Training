from abc import ABC, abstractmethod


class Robot:

    def __init__(self):

        self.bipedal = False
        self.quadripedal = False
        self.wheeled = False
        self.flying = False
        self.traversal = []
        self.detection_systems = []

    def __str__(self):
        string = ""
        if self.bipedal:
            string += "BIPEDAL "
        if self.quadripedal:
            string += "QUADRIPEDAL "
        if self.flying:
            string += "FLYING ROBOT "
        if self.wheeled:
            string += "ROBOT ON WHEELS\n"
        else:
            string += "ROBOT\n"

        if self.traversal:
            string += "Traversal modules installed:\n"

        for module in self.traversal:
            string += "- " + str(module) + "\n"

        if self.detection_systems:
            string += "Detection systems installed:\n"

        for system in self.detection_systems:
            string += "- " + str(system) + "\n"

        return string


class BipedalLegs:
    def __str__(self):
        return "two legs"


class QuadripedalLegs:
    def __str__(self):
        return "four legs"


class Arms:
    def __str__(self):
        return "four legs"


class Wings:
    def __str__(self):
        return "wings"


class Blades:
    def __str__(self):
        return "blades"


class FourWheels:
    def __str__(self):
        return "four wheels"


class TwoWheels:
    def __str__(self):
        return "two wheels"


class CameraDetectionSystem:
    def __str__(self):
        return "cameras"


class InfraredDetectionSystem:
    def __str__(self):
        return "infrared"


class RobotBuilder(ABC):

    @abstractmethod
    def reset(self):
        '''Reset the robot system'''
    
    @abstractmethod
    def build_traversal(self):
        '''Build the traversal system'''

    @abstractmethod
    def build_detection_system(self):
        '''Build the detection system'''


class AndroidBuilder(RobotBuilder):

    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    def build_traversal(self):
        self.product.bipedal = True
        self.product.traversal.append(BipedalLegs())
        self.product.traversal.append(Arms())

    def build_detection_system(self):
        self.product.detection_systems.append(CameraDetectionSystem())


android = AndroidBuilder()
android.build_traversal()
android.build_detection_system()
print(android.product)
