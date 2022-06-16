from abc import ABC, abstractmethod 


class Device(ABC):

    @abstractmethod 
    def connect(self):
        ... 

    @abstractmethod 
    def disconnect(self):
        ...

    @abstractmethod 
    def say_hello(self):
        ...