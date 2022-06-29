from __future__ import annotations
from typing import List, Tuple


class Node:
    def __init__(self, val: int, neighbors: List[Node] | None = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self) -> str:
        return f"""Node(val: {self.val},
        neighbors: {self.neighbors})"""

    def __repr__(self) -> str:
        return f"{self.val}"


class Graph:
    def __init__(self) -> None:
        self.nodes: List[Node] = []

    def get_or_create_node(self, node_val: int) -> Node:
        for node in self.nodes:
            if node.val == node_val:
                return node
        node = Node(node_val)
        self.nodes.append(node)
        return node

    def add_edge(self, org_node_val: int, dest_node_val: int) -> Graph:

        org_node = self.get_or_create_node(org_node_val)
        dest_node = self.get_or_create_node(dest_node_val)
        org_node.neighbors.append(dest_node)

        return self

    def __str__(self):
        result = "Graph: \n"
        for node in self.nodes:
            result += str(node) + "\n"

        return result

    def has_cycle(self) -> bool:
        def dfs(node: Node):
            if node.val in seen:
                return False
            seen.append(node.val)
            ans = 0
            for neighbor in node.neighbors:
                ans += dfs(neighbor)

            return ans == len(node.neighbors)

        for node in self.nodes:
            seen = []
            if not dfs(node):
                return True

        return False


def solution(num_courses: int, prerequisites: List[List[int]]) -> bool:
    relation = {}
    for target, req in prerequisites:
        relation[target] = relation.get(target, []) + [req]

    def has_loop(course: int, seen: Tuple[int] = None) -> bool:
        if seen is None:
            seen = tuple()
        if course in seen:
            return True
        seen = list(seen)
        seen.append(course)
        seen = tuple(seen)
        for prereq in relation.get(course, []):
            if has_loop(prereq, seen):
                return True

        return False

    for course in relation.keys():
        if has_loop(course):
            print(course)
            return False

    return True


# graph = Graph()
# num_courses =
# graph.add_edge(1, 2)
# # graph.add_edge(2, 1)
# print(graph)
# print(graph.has_cycle())

num_courses = 3
prerequisites = [[1, 0], [0, 2], [2, 1]]
print(solution(num_courses, prerequisites))


num_courses = 2
prerequisites = [[1, 0]]
print(solution(num_courses, prerequisites))

num_courses = 5
prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
print(solution(num_courses, prerequisites))
