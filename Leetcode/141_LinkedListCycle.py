from __future__ import annotations


class ListNode:
    def __init__(self, val: int, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        values = []
        hashmap = {}
        node = self
        while node:
            values.append(str(node.val))
            if node in hashmap:
                break
            hashmap[node] = True
            node = node.next
        else:
            values.append("None")
        return " -> ".join(values)

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def has_cycle(root: ListNode) -> bool:
    """Determines wheter a linked list contains a cycle or not."""
    hashmap = {}
    node = root
    while node:
        if node in hashmap:
            return True
        hashmap[node] = True
        node = node.next
    return False


def has_cycle_efficient(root: ListNode) -> bool:
    slow, fast = root, root
    start = True
    while start or (slow is not fast):
        start = False
        try:
            slow = slow.next
            fast = fast.next.next
        except AttributeError as e:
            return False
    return True


root = ListNode(3)
node_2 = ListNode(2)
root.next = node_2
root.next.next = ListNode(0)
root.next.next.next = ListNode(4)
root.next.next.next.next = node_2
print(root)
print(has_cycle(root))
print(has_cycle_efficient(root))


root = ListNode(1)
root.next = node_2
root.next.next = root
print(root)
print(has_cycle(root))
print(has_cycle_efficient(root))

root = ListNode(1)
print(root)
print(has_cycle(root))
print(has_cycle_efficient(root))

print(has_cycle(None))
print(has_cycle_efficient(root))
