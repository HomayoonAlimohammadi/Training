class Node:
    def __init__(self, val: int):
        self.val = val
        self.both = 0


class XORLinkedList:
    def __init__(self, root: Node) -> None:
        self.head = root
        self.tail = root
        self.length = 1

    def add(self, element: int) -> None:
        """Add an element to the end."""
        new_node = Node(element)
        if self.length < 2:
            self.tail = new_node
            return

        self.tail.both = 0

    def get(self, index: int) -> Node:
        """Return a `Node` at the given index."""
        pass


def get_pointer(node: Node) -> str:
    return bin(node.val)


def dereference_pointer(pointer: int) -> None:
    pass
