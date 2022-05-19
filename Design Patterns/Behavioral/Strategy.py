from __future__ import annotations
from abc import ABC, abstractmethod


class Context:

    def __init__(self, initialStrategy: Strategy) -> None:
        self._strategy = initialStrategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def doSomething(self, data: str):
        print('Context: doing something important...')
        self._strategy.doSomething(data)


class Strategy(ABC):

    @abstractmethod
    def doSomething(self, data: str) -> None:
        pass


class ConcreteStrategyA(Strategy):

    def doSomething(self, data: str) -> None:
        print('StrategyA: handling the data...')
        print(f'StrategyA: the data was handled: {data}')


class ConcreteStrategyB(Strategy):

    def doSomething(self, data: str) -> None:
        print('StrategyB: handling the data...')
        print(f'StrategyB: the data was handled: {data}')


if __name__ == '__main__':

    strA = ConcreteStrategyA()
    strB = ConcreteStrategyB()
    context = Context(strA)

    context.doSomething('Hello')
    context.strategy = strB
    context.doSomething('Hello again')