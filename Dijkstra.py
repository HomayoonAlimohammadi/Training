from __future__ import annotations
from typing import List, Set, Union
import heapq


class Node:
    '''
    Implementation of every node in the Graph.
    '''
    def __init__(self, val: int) -> None:
        self.val = val
        self.adj: Set[Node] = set()
        self.edges: Set[Edge] = set()

    def get_edge_to(self, dest: Node) -> Edge:
        if not isinstance(dest, Node):
            raise ValueError('`dest` must be an instance of Node.')
        for edge in self.edges:
            if dest in edge.nodes:
                return edge
        raise ValueError(f'No edge from `{self.val}` to `{dest}` found.')

    def __str__(self):
        return f'Node{{val: {self.val}, adj:{self.adj}}}'

    def __repr__(self):
        return f'{self.val}'


class Edge:
    '''
    Edge class for making connections between instances of Nodes.
    '''
    def __init__(self, org_node: Node, dest_node: Node, weight: int = 1) -> None:
        self.nodes: Set[Node] = {org_node, dest_node}
        self.weight = weight

    def __str__(self) -> None:
        org, dest = self.nodes
        return f'Edge{{between {org.val} and {dest.val}, weight: {self.weight}}}'
    
    def __repr__(self) -> None:
        org, dest = self.nodes
        return f'({org.val}, {dest.val})'


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

    def add_edge(self, org_node: Union[Node, int], dest_node: Union[int, Node], weight: int = 1) -> Graph:
        '''Add an edge between two given nodes, given their values.'''

        if isinstance(org_node, int):
            org_node = self.get_node_by_value(org_node)
        if isinstance(dest_node, int):
            dest_node = self.get_node_by_value(dest_node)

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

    def dijkstra(self, source: int) -> List[int]:
        '''Calculate and return shortest path from a given node to all other nodes.'''
        visited = set()
        distances = {source: 0}
        pq = [(0, source)]
        for node in self.nodes:
            val = node.val
            if val == source:
                continue
            distances[val] = float('inf')
        heapq.heapify(pq)
        
        while pq:
            current_dist, val = heapq.heappop(pq)
            if val in visited:
                continue
            visited.add(val)
            node = self.get_node_by_value(val)
            for adj_node in node.adj:
                adj_dist = distances[adj_node.val]
                edge = node.get_edge_to(adj_node)
                if current_dist + edge.weight < adj_dist:
                    distances[adj_node.val] = current_dist + edge.weight
                heapq.heappush(pq, (distances[adj_node.val], adj_node.val))
        return distances

    def __str__(self) -> None:
        result = 'Graph: {\n'
        for node in self.nodes:
            result += str(node) + '\n'
        return result + '}'

    def __repr__(self) -> None:
        return str(self.nodes)
    

graph = Graph()
graph.add_node(0)
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)
graph.add_node(6)
graph.add_node(7)
graph.add_node(8)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 6, 7)
graph.add_edge(1, 2, 9)
graph.add_edge(1, 7, 20)
graph.add_edge(1, 6, 11)
graph.add_edge(2, 4, 2)
graph.add_edge(2, 3, 6)
graph.add_edge(3, 4, 10)
graph.add_edge(3, 5, 5)
graph.add_edge(4, 5, 15)
graph.add_edge(4, 7, 1)
graph.add_edge(4, 8, 5)
graph.add_edge(5, 8, 12)
graph.add_edge(6, 7, 1)
graph.add_edge(7, 8, 3)
node_1 = graph.get_node_by_value(1)
node_2 = graph.get_node_by_value(2)
# print(node_2.get_edge_to(node_1))
distances = graph.dijkstra(0)
for key in sorted(distances.keys()):
    print(f'{key}: {distances[key]}')
# print(graph)
