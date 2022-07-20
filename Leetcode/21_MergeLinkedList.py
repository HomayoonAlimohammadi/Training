from __future__ import annotations


class ListNode:
    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        values = []
        node = self
        while node:
            values.append(str(node.val))
            node = node.next
        values.append(str(None))
        return " -> ".join(values)


def merge_linked_lists(list1: ListNode, list2: ListNode) -> ListNode:
    if not list1 and not list2:
        return None
    if not list1 or not list2:
        return list1 or list2

    if list1.val < list2.val:
        merged_list = ListNode(list1.val)
        list1 = list1.next
    else:
        merged_list = ListNode(list2.val)
        list2 = list2.next

    merged_list_root = merged_list
    while list1 and list2:
        if list1.val < list2.val:
            merged_list.next = ListNode(list1.val)
            list1 = list1.next
        else:
            merged_list.next = ListNode(list2.val)
            list2 = list2.next

        merged_list = merged_list.next

    merged_list.next = list1 or list2
    return merged_list_root


root1 = ListNode(1)
root1.next = ListNode(2)
root1.next.next = ListNode(4)

root2 = ListNode(1)
root2.next = ListNode(3)
root2.next.next = ListNode(4)
print(merge_linked_lists(root1, root2))


root1 = ListNode(1)
root2 = ListNode(3)
print(merge_linked_lists(root1, root2))

root1 = None
root2 = None
print(merge_linked_lists(root1, root2))

root1 = ListNode(2)
root2 = None
print(merge_linked_lists(root1, root2))
