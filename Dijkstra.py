from __future__ import annotations
from typing import List


class Node:
    '''
    Implementation of every node in the Graph.
    '''
    def __init__(self, val: int) -> None:
        self.val = val
        self.adj = set()
        self.edges = set()

    def __str__(self):
        return f'Node{{val: {self.val}, adj:{self.adj}}}'

    def __repr__(self):
        return f'{self.val}'


class Edge:
    '''
    Edge class for making connections between instances of Nodes.
    '''
    def __init__(self, org_node: Node, dest_node: Node, weight: int = 1) -> None:
        self.org = org_node
        self.dest = dest_node
        self.weight = weight

    def __str__(self) -> None:
        return f'Edge{{from: {self.org.val}, to: {self.dest.val}, weight: {self.weight}}}'
    
    def __repr__(self) -> None:
        return f'({self.org.val}, {self.dest.val})'


class Graph:
    '''
    Graph class for managing connected Nodes.
    '''
    def __init__(self, nodes: List[int] = None) -> None:
        self.nodes = set()
        if nodes:
            for val in nodes:
                node = Node(val)
                self.nodes.add(node)

    @property
    def order(self) -> int:
        '''Return the order of the graph.'''
        return len(self.nodes)

    def add_node(self, val: int) -> Graph:
        '''Add a Node to the graph with the given value as Node's value.'''
        node = Node(val)
        self.nodes.add(node)
        return self

    def add_edge(self, org: int, dest: int, weight: int = 1) -> Graph:
        '''Add an edge between two given nodes, given their values.'''
        org_node = self.get_node_by_value(org)
        dest_node = self.get_node_by_value(dest)

        edge = Edge(org_node, dest_node, weight)

        org_node.adj.add(dest_node)
        dest_node.adj.add(org_node)
        org_node.edges.add(edge)
        dest_node.edges.add(edge)

        return self

    def get_node_by_value(self, val: int) -> Node:
        '''Return a Node obj given it's value.'''
        for node in self.nodes:
            if node.val == val:
                return node
        raise ValueError(f'Node with the value of `{val}` does not exist in the graph.')

    def __str__(self) -> None:
        result = 'Graph: {\n'
        for node in self.nodes:
            result += str(node) + '\n'
        return result + '}'

    def __repr__(self) -> None:
        return str(self.nodes)
    

graph = Graph()
graph.add_node(1)
graph.add_node(2)
graph.add_edge(1, 2)
