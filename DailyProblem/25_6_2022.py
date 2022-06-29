from __future__ import annotations
from typing import Dict, Tuple


class Node:
    def __init__(self, val: int, left: Node | None = None, right: Node | None = None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self):
        return f"""
    Node{{val: {self.val},
        left: {self.left},
        right: {self.right}}}"""


def check_universal(node: Node, num_universal: int = 0) -> Dict[str, bool | int]:

    if node.left is None and node.right is None:
        return {"is_universal": True, "val": node.val, "num_universal": num_universal}

    left_node, right_node = None, None
    if node.left is not None:
        left_node = check_universal(node.left)

    if node.right is not None:
        right_node = check_universal(node.right)

    if left_node is None:
        left_node = right_node
        num_universal = right_node["num_universal"]
    elif right_node is None:
        right_node = left_node
        num_universal = left_node["num_universal"]
    else:
        num_universal = left_node["num_universal"] + right_node["num_universal"]

    is_universal = False
    if left_node["is_universal"] and right_node["is_universal"]:
        num_universal += left_node["val"] == right_node["val"]
        is_universal = True

    return {
        "val": node.val,
        "is_universal": is_universal,
        "num_universal": num_universal,
    }


def count_universal_subtrees(node: Node) -> Tuple[bool, int]:
    if node is None:
        return (True, 0)

    left_node = count_universal_subtrees(node.left)
    right_node = count_universal_subtrees(node.right)

    this_tree = (
        left_node[0]
        and right_node[0]
        and (node.left is None or node.val == node.left.val)
        and (node.right is None or node.val == node.right.val)
    )

    return (this_tree, left_node[1] + right_node[1] + this_tree)


def main():
    graph = Node(
        0,
        left=Node(1),
        right=Node(1, left=Node(1, left=Node(1), right=Node(1)), right=Node(1)),
    )

    # print(graph)
    result = check_universal(graph)
    result_2 = count_universal_subtrees(graph)
    print(result)
    print(result_2)


if __name__ == "__main__":
    main()
