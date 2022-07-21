from __future__ import annotations
from collections import deque


class TreeNode:
    def __init__(
        self, val: int, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        values = []
        nodes = deque([self])
        while nodes:
            node = nodes.popleft()
            if node:
                value = node.val
                nodes.append(node.left)
                nodes.append(node.right)
            else:
                value = node
            values.append(value)
        while values[-1] is None:
            values.pop()
        return str(values)


def calculate_tree_diameter(root: TreeNode) -> int:
    def dfs(node: TreeNode) -> tuple[int, int]:
        left_depth, right_depth = 0, 0
        left_longest_path, right_longest_path = 0, 0
        max_depth, longest_path_from_here = 0, 0
        if node.left:
            left_depth, left_longest_path = dfs(node.left)
            left_depth += 1
        if node.right:
            right_depth, right_longest_path = dfs(node.right)
            right_depth += 1

        if node.left or node.right:
            max_depth = max(left_depth, right_depth)
            longest_path_from_here = max(
                left_longest_path, right_longest_path, left_depth + right_depth
            )
        return max_depth, longest_path_from_here

    return max(dfs(root))


root = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_2.left = node_4
node_2.right = node_5
root.left = node_2
root.right = node_3

print(root)
print(calculate_tree_diameter(root))
