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

    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        Reorder the ListNode 
        from: L0 → L1 → … → Ln - 1 → Ln
        to: L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
        '''
        # values = []
        # while head:
        #     values.append(head.val)
        #     head = head.next

        # head = None
        

        # return head

        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        # curr = head
        # i = 0
        # while curr and values:
        #     i += 1
        #     node = ListNode(values[-1])
        #     values.pop()
        #     if i % 2 == 0:
        #         node.next = None
        #     else:
        #         node.next = curr.next

        #     print(i)
        #     print(node)
        #     curr.next = node
        #     curr = curr.next
        #     curr = curr.next

        values.pop(0)
        curr = head
        print(values)
        for i in range(len(values)):
            if i % 2 == 0:
                val = values[-1]
                values.pop()
            else:
                val = values[0]
                values.pop(0)

            node = ListNode(val, None)
            curr.next = node
            curr = node
        
        return head


        

def create_linked_list(values):

    head = None
    for val in values:
        if head is None:
            head = ListNode(val, None)
            curr = head
        else:
            node = ListNode(val, None)
            curr.next = node
            curr = node
    
    return head


values = [1,2,3,4]
head = create_linked_list(values)
head_reordered = Solution().reorderList(head)
print(head_reordered)
