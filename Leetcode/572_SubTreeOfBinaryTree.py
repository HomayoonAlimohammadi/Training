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


def is_sub_tree_of(ref: TreeNode | None, target: TreeNode | None) -> bool:
    def is_same_tree(root1: TreeNode | None, root2: TreeNode | None) -> bool:
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

    def check_node(node: TreeNode | None, lookup: TreeNode | None) -> bool:
        if node is None:
            return lookup is None

        lookup_val = None
        if lookup:
            lookup_val = lookup.val
        if node.val == lookup_val:
            if is_same_tree(node, lookup):
                return True
        left_has_sub_tree = check_node(node.left, lookup)
        right_has_sub_tree = check_node(node.right, lookup)

        return left_has_sub_tree or right_has_sub_tree

    return check_node(ref, target)


def is_sub_tree_of_2(ref: TreeNode | None, target: TreeNode | None) -> bool:
    candids = deque([])
    ref_nodes = deque([ref])
    while ref_nodes:
        node = ref_nodes.popleft()
        new_candids = deque([])
        while candids:
            candid = candids.popleft()
            if node and candid:
                ...
