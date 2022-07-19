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


def invert_binary_tree(root: TreeNode) -> TreeNode:
    nodes = deque([root])
    while nodes:
        node = nodes.popleft()
        if not node:
            continue
        node.left, node.right = node.right, node.left
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)

    return root


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

print(root)
invert_binary_tree(root)
print(root)
