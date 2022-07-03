from typing import List


def solution(edges: List[List[int]]) -> List[int]:
    """
    Return a redundant graph which removing it
    converts the previously cycled graph into a tree.
    """
    graph = {}
    for vert_1, vert_2 in edges:
        graph[vert_1] = graph.get(vert_1, []) + [vert_2]
        graph[vert_2] = graph.get(vert_2, []) + [vert_1]

    visited = []
    print(graph)

    def has_loop(node: int, prev_node: int | None = None) -> bool:
        """Return if `node` is part of a loop."""
        if not graph.get(node, []):
            return False
        if node in visited:
            return True

        visited.append(node)
        for adj_node in graph.get(node, []):
            if adj_node == prev_node:
                continue
            if has_loop(adj_node, node):
                return True

        visited.pop()
        graph[node] = []
        return False

    for node in graph:
        if has_loop(node):
            print(f"found loop: {visited}")
            for vert_1, vert_2 in reversed(edges):
                if vert_1 in visited and vert_2 in visited:
                    return [vert_1, vert_2]
    print("no loops found :(")
    return visited


edges = [[1, 2], [1, 3], [2, 3]]
print(solution(edges))

edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
print(solution(edges))


edges = [
    [30, 44],
    [34, 47],
    [22, 32],
    [35, 44],
    [26, 36],
    [2, 15],
    [38, 41],
    [28, 35],
    [24, 37],
    [14, 49],
    [44, 45],
    [11, 50],
    [20, 39],
    [7, 39],
    [19, 22],
    [3, 17],
    [15, 25],
    [1, 39],
    [26, 40],
    [5, 14],
    [6, 23],
    [5, 6],
    [31, 48],
    [13, 22],
    [41, 44],
    [10, 19],
    [12, 41],
    [1, 12],
    [3, 14],
    [40, 50],
    [19, 37],
    [16, 26],
    [7, 25],
    [22, 33],
    [21, 27],
    [9, 50],
    [24, 42],
    [43, 46],
    [21, 47],
    [29, 40],
    [31, 34],
    [9, 31],
    [14, 31],
    [5, 48],
    [3, 18],
    [4, 19],
    [8, 17],
    [38, 46],
    [35, 37],
    [17, 43],
]
print(solution(edges))
