"""
A module containing `serialize` and `deserialize` functions to 
cast on a root `Node` object.
`Serialize`: Transforms a root `Node` object into a comma separated string.
`Deserialize`: Transforms a comma separated string representing a tree, 
to an actual root `Node` object.
"""
from __future__ import annotations
from collections import deque


class Node:
    def __init__(self, val: int, left: Node = None, right: Node = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"""Node(val: {self.val},
            left: {self.left},
            right: {self.right}
        )"""

    def __repr__(self) -> str:
        return f"Node({self.val})"


def serialize(root: Node) -> str:
    """Transforms a root `Node` object into a comma separated string"""
    result = [f"{root.val}"]
    nodes = deque([root])
    while nodes:
        curr_node = nodes.popleft()
        if curr_node.left:
            result.append(curr_node.left.val)
            nodes.append(curr_node.left)
        else:
            result.append("None")

        if curr_node.right:
            result.append(curr_node.right.val)
            nodes.append(curr_node.right)
        else:
            result.append("None")

    result = [str(val) for val in result]
    return ", ".join(result)


def deserialize(string: str) -> Node:
    """
    Transforms a comma separated string representing a tree, to an
    actual root `Node` object.
    """
    values = deque(string.split(", "))
    root_val = values.popleft()
    root = Node(root_val)
    nodes = deque([root])
    while nodes:
        curr_node = nodes.popleft()

        try:
            left_val = values.popleft()
        except IndexError:
            break
        if left_val != "None":
            left = Node(left_val)
            curr_node.left = left
            nodes.append(left)

        try:
            right_val = values.popleft()
        except IndexError:
            break
        if right_val != "None":
            right = Node(right_val)
            curr_node.right = right
            nodes.append(right)

    return root


node_4 = Node(4)
node_2 = Node(2)
node_5 = Node(5)
node_0 = Node(0)
node_1 = Node(1)
node_7 = Node(7)

node_0.left = node_5
node_0.right = node_1
node_5.left = node_4
node_5.right = node_2
node_1.right = node_7

serialized = serialize(node_0)
print(serialized)
deserialized = deserialize(serialized)
print(deserialized)

print(node_4.val, type(node_4.val))
print(deserialized.left.left.val, type(deserialized.left.left.val))
assert str(deserialized.left.left.val) == str(node_4.val)
