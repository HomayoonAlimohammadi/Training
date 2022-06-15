from __future__ import annotations
from typing import List


class Node:
    def __init__(self, val: int = 0, neighbors: List[Node] = None) -> None:
        self.val = val 
        self.neighbors = neighbors if neighbors else [] 

    def __str__(self):
        return str(self.neighbors)

    def __repr__(self):
        return str(self.neighbors)


class Solution:
    def clone_graph(self, node: Node) -> Node:

        if node is None:
            return None

        graph = {}
        def copy(node: 'Node') -> 'Node':
            copy_node = Node(node.val)
            graph[node.val] = copy_node
            for neighbor in node.neighbors:
                if neighbor.val in graph:
                    copy_neighbor = graph[neighbor.val]
                else:
                    copy_neighbor = copy(neighbor)
                copy_node.neighbors.append(copy_neighbor)
                    
            return copy_node
        
        copy_node = copy(node)
        return copy_node


