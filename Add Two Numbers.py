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
    def addTwoNumbers(self,l1,l2):
        l1_list = []
        l2_list = []
        l_final = []
        while l1 != None:
            l1_list.append(l1.val)
            l1 = l1.next
        while l2 != None:
            l2_list.append(l2.val)
            l2 = l2.next
        
        l1_list = [int(num) for num in l1_list]
        l2_list = [int(num) for num in l2_list]
        if len(l1_list)>len(l2_list):
            l2_list += [0] * (len(l1_list) - len(l2_list))
        elif len(l2_list)>len(l1_list):
            l1_list += [0] * (len(l2_list) - len(l1_list))
        
        print(l1_list,l2_list)
        l_final = []
        save = 0
        while len(l1_list) != 0 and len(l2_list) != 0:
            num = l1_list[0] + l2_list[0] + save
            save = num//10
            l_final.append(num%10)
            l1_list = l1_list[1:]
            l2_list = l2_list[1:]
        if save == 1:
            l_final.append(save)
        print(l_final)
        l_final = list_to_LL(l_final)    
        return l_final
