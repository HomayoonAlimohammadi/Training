from __future__ import annotations
from collections import defaultdict
from typing import List, Set


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
        relation[target] = relation.get(target, []) + [req]  # type: ignore

    def has_loop(node: int, visit_set: Set[int]):
        if node in visit_set:
            return True
        if node in total_visit:
            return False
        visit_set.add(node)
        total_visit.add(node)
        prereq: int
        for prereq in relation.get(node, []):  # type: ignore
            if has_loop(prereq, visit_set.copy()):
                return True

        return False

    total_visit: Set[int] = set()
    course: int
    for course in range(num_courses):
        if course not in total_visit:
            if has_loop(course, set()):
                return False

    return True


def solution_better(num_courses: int, prerequisites: List[List[int]]) -> bool:
    adj_list = {}
    for i in range(num_courses):
        adj_list[i] = []

    for c1, c2 in prerequisites:
        adj_list[c1].append(c2)

    visited = set()

    def dfs(course):
        if len(adj_list[course]) == 0:
            return True
        if course in visited:
            return False

        visited.add(course)
        for nei in adj_list[course]:
            if dfs(nei) == False:
                return False
        visited.remove(course)
        adj_list[course] = []
        return True

    for i in adj_list:
        if dfs(i) == False:
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
