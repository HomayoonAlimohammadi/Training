from __future__ import annotations 
from typing import List, Tuple, Set, Union, Dict
from math import sqrt 
from collections import deque


class Coordination:
    '''Coordination class for specifying coordinates for instances of Node.'''
    def __init__(self, x: int, y: int):
        self.x = x 
        self.y = y 

    def __str__(self):
        return f'({self.x}, {self.y})'


class Node:
    '''
    Node class which is a subset of a graph.
    Nodes can be connected via edges with a certain value (weight).
    '''
    def __init__(self, name: str, adj_nodes: Dict[Node, int], coord: Tuple[int]):
        self.name = name 
        self.adj_nodes = adj_nodes 
        self.coord = coord 
    
    def add_adj(self, *args: List[Tuple(Union[Node, int])]):
        for node, dist in args:
            if not isinstance(node, Node):
                raise ValueError('Only nodes can be added to adjacency list.')
            if node not in self.adj_nodes:
                self.adj_nodes[node] = dist
                node.add_adj((self, dist))

    def __str__(self):
        if self.adj_nodes:
            res =  f'Node{{{self.name}: ('
            for node, dist in self.adj_nodes.items():
                res += f'({node.name}, {dist}), '
            res = res[:-2] + ')}'
            return res
        return f'Node{{{self.name}: ()}}'

    def __repr__(self):
        return f'{self.name}'


class Graph:
    '''
    Graph class which contains instances of Nodes.
    '''
    def __init__(self, nodes: Set(Node)):
        self.nodes = nodes 

    def h(self, node: Node, goal: Node):
        dx = abs(node.coord.x - goal.coord.x)
        dy = abs(node.coord.y - goal.coord.y)

        return sqrt(dx**2 + dy**2)

    def f(self, start: Node, mid: Node, end: Node):
        return start.adj_nodes[mid] + self.h(mid, end)

    def a_star_shortest_path(self, start: Node, end: Node):
        '''A* Algorithm for graph traversal'''
        if start not in self.nodes or end not in self.nodes:
            raise ValueError('`start` and `end` nodes must be in the graph.')
        
        seen = set()
        nodes_data = {}

        def traverse(node: Node, goal: Node, path: Union[List[Node], None] = None):
            if node == goal:
                return path
            if path is None:
                path = [node]

            if node not in seen:
                seen.add(node)
                nodes_data[node] = []
                for adj_node in node.adj_nodes:
                    if adj_node not in seen:
                        f = self.f(node, adj_node, goal)
                        nodes_data[node].append((adj_node, f))
                nodes_data[node].sort(key = lambda x: x[1])
                if not nodes_data[node]:
                    return path

            choice, _ = nodes_data[node].pop(0)
            path.append(choice)
            path = traverse(choice, goal, path.copy())
            return path
        
        return traverse(start, end)

    def __str__(self):
        res = 'Graph: {\n'
        for node in self.nodes:
            res += str(node) + '\n'
        res += '}'
        return res
            


node_a = Node('A', {}, Coordination(0, 0))
node_b = Node('B', {}, Coordination(1, 1))
node_c = Node('C', {}, Coordination(2, 2))
node_d = Node('D', {}, Coordination(3, -1))

node_a.add_adj((node_b, 2), (node_d, 5))
node_b.add_adj((node_c, 3), (node_d, 4))
print(node_a)
print(node_b)
print(node_c)
print(node_d)
graph = Graph({node_a, node_b, node_c, node_d})
print(graph)
print(graph.f(node_a, node_d, node_d))
print(graph.f(node_a, node_b, node_d))
print(graph.f(node_b, node_d, node_d))
print(graph.a_star_shortest_path(node_a, node_d))