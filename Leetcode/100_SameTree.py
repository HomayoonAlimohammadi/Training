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
        nodes = deque([self])
        values = []
        while nodes:
            node = nodes.popleft()
            if node:
                values.append(node.val)
                nodes.append(node.left)
                nodes.append(node.right)
            else:
                values.append(node)
        while values[-1] is None:
            values.pop()

        return str(values)


def is_same_tree(root1: TreeNode, root2: TreeNode) -> bool:
    return str(root1) == str(root2)


def is_same_tree_again(root1: TreeNode, root2: TreeNode) -> bool:
    tree_1_nodes = deque([root1])
    tree_2_nodes = deque([root2])
    while tree_1_nodes and tree_2_nodes:
        node_1 = tree_1_nodes.popleft()
        node_2 = tree_2_nodes.popleft()
        if type(node_1) != type(node_2):
            return False
        if node_1 is not None:  # then node_2 is not None neither
            if node_1.val != node_2.val:
                return False
            tree_1_nodes.append(node_1.left)
            tree_1_nodes.append(node_1.right)

            tree_2_nodes.append(node_2.left)
            tree_2_nodes.append(node_2.right)
    return not tree_1_nodes and not tree_2_nodes


root = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
root.left = node_2
node_2.right = node_3
print(root)
