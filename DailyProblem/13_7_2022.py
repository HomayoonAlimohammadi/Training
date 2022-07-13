from __future__ import annotations


class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def copy(self) -> ListNode:
        new_root = ListNode(self.val)
        new_node = new_root
        curr = self.next
        while curr:
            new_node.next = ListNode(curr.val)
            new_node = new_node.next
            curr = curr.next
        return new_root

    def __repr__(self) -> str:
        result = ""
        node = self
        while node:
            result += f"{node.val} -> "
            node = node.next
        return result + "None"

    def __str__(self) -> str:
        return f"ListNode({self.val} -> {self.next})"


def solution(root: ListNode, k: int) -> ListNode:
    prev_node, end_flag = root, root
    for _ in range(k + 1):
        try:
            end_flag = end_flag.next
        except AttributeError as e:
            return root.next

    while end_flag:
        end_flag = end_flag.next
        prev_node = prev_node.next

    prev_node.next = prev_node.next.next
    return root


root = ListNode(10)
node_20 = ListNode(20)
node_30 = ListNode(30)
node_40 = ListNode(40)
node_50 = ListNode(50)
node_40.next = node_50
node_30.next = node_40
node_20.next = node_30
root.next = node_20
print("base root:", repr(root))
MAX_K = 5
for k in range(1, MAX_K + 1):
    old_root = root.copy()
    new_root = solution(old_root, k)
    print(f"pop {k}th element:", repr(new_root))
