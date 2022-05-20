'''
This is code example for Visitor design pattern
'''

from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod


class Component(ABC):
    '''
    Component Interface
    '''

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        '''Abstract accept() method'''


class BaseComponent(Component):
    '''
    BaseComponent with default doSomething() method
    '''

    @property
    def component_id(self) -> str:
        '''ID property for Components'''
        return self._id

    def do_something(self) -> None:
        '''Default behavior for do_something() method.'''
        print(f'{self._id}: doing something important...')


class ConcreteComponentA(BaseComponent):
    '''ConcreteComponentA with specific accept method'''

    def __init__(self) -> None:
        self._id = 'ComponentA'

    def accept(self, visitor: Visitor) -> None:
        '''ConcreteComponentA accept() method'''
        print(f'ComponentA: Accepting {visitor.visitor_id}...')
        visitor.visit_component_A(self)


class ConcreteComponentB(BaseComponent):
    '''ConcreteComponentB with specific accept method'''

    def __init__(self) -> None:
        self._id = 'ComponentB'

    def accept(self, visitor: Visitor) -> None:
        '''ConcreteComponentB accept method'''
        print(f'ComponentB: accepting {visitor.visitor_id}...')
        visitor.visit_component_B(self)


class Visitor(ABC):
    '''Visitor Interface'''

    @abstractmethod
    def visit_component_A(self, component: Component) -> None:
        '''visitComponentA abstract method'''

    @abstractmethod
    def visit_component_B(self, component: Component) -> None:
        '''visitComponentB abstract method'''


class BaseVisitor(Visitor):
    '''BaseVisitor class'''

    @property
    def visitor_id(self) -> str:
        return self._id

    def visit_component_A(self, component: Component) -> None:
        '''visitComponentA default behavior'''
        print(f'{self._id}: visiting {component.component_id}')
        component.do_something()

    def visit_component_B(self, component: Component) -> None:
        '''visitComponentB default behavior'''
        print(f'{self._id}: visiting {component.component_id}')
        component.do_something()


class ConcreteVisitorA(BaseVisitor):
    '''ConcreteVisitorA with specific visit methods'''

    def __init__(self) -> None:
        self._id = 'VisitorA'


class ConcreteVisitorB(BaseVisitor):
    '''ConcreteVisitorB with specific visit methods'''

    def __init__(self) -> None:
        self._id = 'VisitorB'


def client(components: List[Component], visitor: Visitor):
    '''client code for managing components and visitors'''
    for component in components:
        component.accept(visitor)
        print()


if __name__ == '__main__':

    visitorA = ConcreteVisitorA()
    visitorB = ConcreteVisitorB()

    componentA = ConcreteComponentA()
    componentB = ConcreteComponentB()

    components = [componentA, componentB]

    client(components, visitorA)
    client(components, visitorB)
