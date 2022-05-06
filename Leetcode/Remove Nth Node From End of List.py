from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"


def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_list = []
        while head != None:
            head_list.append(head.val)
            head = head.next
        if n == 1:
            print(head_list[:-1])
            return list_to_LL(head_list[:-1])
        head_list = head_list[:-n] + head_list[-n+1:]
        print(head_list)
        return list_to_LL(head_list)
    
    
head, n = [1,2,3,4,5], 1
head = list_to_LL(head)
S = Solution()
ans = S.removeNthFromEnd(head,n)
print(ans)
