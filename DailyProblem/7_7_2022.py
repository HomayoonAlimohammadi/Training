from __future__ import annotations
from typing import List, Optional


class Node:
    def __init__(self, val: int, next: Node = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"Node(val: {self.val})"

    def __str__(self) -> str:
        return f"Node(val: {self.val}, next: {self.next})"


class LinkedList:
    def __init__(self, head: Node) -> None:
        self.head = head

    @classmethod
    def convert_to_linked_list(cls, val_list: List[int]) -> Node:
        current = Node(val_list[0])
        linked_list = cls(current)
        for val in val_list[1:]:
            new_node = Node(val)
            current.next = new_node
            current = new_node

        return linked_list

    @staticmethod
    def find_intersection_with(head_A: Node, head_B: Node) -> Optional[Node]:
        hash_set = set()
        while head_A:
            hash_set.add(hash(head_A))
            head_A = head_A.next

        while head_B:
            if hash(head_B) in hash_set:
                return head_B
            head_B = head_B.next

    @staticmethod
    def find_intersection_with_optimized(head_A: Node, head_B: Node) -> Optional[Node]:
        len_A, len_B = 0, 0
        node = head_A
        while node:
            len_A += 1
            node = node.next

        node = head_B
        while node:
            len_B += 1
            node = node.next

        if len_A >= len_B:
            for _ in range(len_A - len_B):
                head_A = head_A.next

        else:
            for _ in range(len_B - len_A):
                head_B = head_B.next

        while head_A:
            if head_A is head_B:
                return head_A
            head_A = head_A.next
            head_B = head_B.next

    @staticmethod
    def find_intersection_with_even_better(
        head_A: Node, head_B: Node
    ) -> Optional[Node]:
        l1, l2 = head_A, head_B
        while l1 is not l2:
            l1 = l1.next if l1 else head_B
            l2 = l2.next if l2 else head_A
        return l1

    def __str__(self) -> str:
        result = "["
        node = self.head
        while node:
            result += f"{node.val}, "
            node = node.next
        result = result[:-2] + "]"
        return result
