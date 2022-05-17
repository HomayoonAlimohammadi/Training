from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self):
        print(f'SimpleCommand is doing task {self._payload}...')
        sleep(1)


class ComplexCommand(Command):

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self):
        print('ComplexCommand is delegating some work to the receiver...')
        sleep(1)
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:

    def do_something(self, a):
        print(f'Receiver is doing something: {a}...')
        sleep(1)

    def do_something_else(self, b):
        print(f'Receiver is doing something else: {b}...')
        sleep(1)


class Invoker:

    _on_start: Command = None
    _on_finish: Command = None

    def set_on_start(self, command: Command) -> None:
        self._on_start = command

    def set_on_finish(self, command: Command) -> None:
        self._on_finish = command

    def do_something_important(self) -> None:

        print('Does anybody want something done before I begin?')
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print('Doing something really important...')
        sleep(2)

        print('Does anybody want something done after I finish?')
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == '__main__':

    receiver = Receiver()
    simpleCommand = SimpleCommand('Simple Task')
    complexCommand = ComplexCommand(
        receiver=receiver, 
        a='Complex Task A',
        b='Complex Task B'
    )
    invoker = Invoker()
    invoker.set_on_start(simpleCommand)
    invoker.set_on_finish(complexCommand)
    invoker.do_something_important()



