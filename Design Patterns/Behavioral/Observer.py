from __future__ import annotations
from random import randrange
from abc import ABC, abstractmethod
from typing import List, Union


class Subject(ABC):

    @abstractmethod
    def subscribe(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):

    _state: int = None
    _observers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self._observer.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def doSomeLogic(self):
        print('Subject: Doing something important...')
        self._state = randrange(1, 100)
        print(f'Subject: My state changed to {self._state}')
        print('Subject: Notifying my observers...')
        self.notify()
        print()


class Observer(ABC):

    @abstractmethod
    def update(self, context: Union[Subject, str]):
        pass


class ConcreteObserverA(Observer):

    def update(self, context: Union[Subject, str]):
        
        if isinstance(context, str):
            print('ConcreteObserverA: Thanks for notification.')
        elif isinstance(context, Subject):
            if context._state > 60:
                print('ConcreteObserverA: Reacting to changes in the Subject.')


class ConcreteObserverB(Observer):

    def update(self, context: Union[Subject, str]):
        
        if isinstance(context, str):
            print('ConcreteObserverB: Thanks for notification.')
        elif isinstance(context, Subject):
            if context._state < 40:
                print('ConcreteObserverB: Reacting to changes in the Subject.')


def main():

    subject = ConcreteSubject()
    obsA = ConcreteObserverA()
    obsB = ConcreteObserverB()

    subject.subscribe(obsA)
    subject.subscribe(obsB)

    for i in range(5):
        subject.doSomeLogic()


if __name__ == '__main__':
    main()