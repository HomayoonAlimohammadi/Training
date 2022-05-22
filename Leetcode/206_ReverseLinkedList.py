from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val} -> {self.next}'

    def __repr__(self):
        return f'{self.val}'


class Solution:

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:

        nums = []
        for node in head:
            nums.append(node.val)
        
        next = None
        result = []
        for num in nums[::-1]:
            node = ListNode(val=num, next=next)
            result.append(node)
            next = node
        
        return result


class Solution2:

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:

        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        last = None
        for num in nums[::-1]:
            if last is None:
                last = ListNode(val=num)
                curr = last
            else:
                node = ListNode(val=num)
                curr.next = node
                curr = node

        return last



func = Solution2().reverse
values = [1,2,3,4]
head = None
for num in values:
    if head is None:
        head = ListNode(val=num)
        curr = head
    else:
        node = ListNode(val=num)
        curr.next = node
        curr = node
        

print(head)
print(func(head))