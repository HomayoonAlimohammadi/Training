from __future__ import annotations
from collections import deque


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode = None, right: TreeNode = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        values = []
        nodes = deque([self])
        while nodes:
            node = nodes.popleft()
            values.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return f"TreeNode: {values}"

    def __repr__(self) -> str:
        return str(self.val)


def maximum_depth_binary_tree(root: TreeNode) -> int:
    def find_depth(node: TreeNode, max_depth: int) -> int:
        if node is None:
            return max_depth
        return max(
            find_depth(node.left, max_depth + 1),
            find_depth(node.right, max_depth + 1),
        )

    max_depth = find_depth(root, 0)
    return max_depth


root = TreeNode(4)
node_2 = TreeNode(2)
node_7 = TreeNode(7)
node_1 = TreeNode(1)
node_3 = TreeNode(3)
node_6 = TreeNode(6)
node_9 = TreeNode(9)

node_2.left = node_1
node_2.right = node_3

node_7.left = node_6
node_7.right = node_9

root.left = node_2
root.right = node_7

print(maximum_depth_binary_tree(root))
