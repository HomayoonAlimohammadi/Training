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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head != None:
            l.append(head.val)
            head = head.next
        l_final = []
        l_last = []
        if len(l) % 2 != 0:
            l_last.append(l[-1])
            for i in range(0,len(l)-1, 2):
                l_final += [l[i+1], l[i]]
        else:
            for i in range(0,len(l), 2):
                l_final += [l[i+1], l[i]]
        l_final += l_last
        
        return list_to_LL(l_final)
        
S = Solution()
head = list_to_LL([1,2,3,4])
ans = S.swapPairs(head)
print(ans)