# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1 is None and list2 is None:
            return None
        
        newHead = ListNode(0)
        p, p1, p2 = newHead, list1, list2
        while p1 != None and p2!=None:
            if p1.val < p2.val:
                p.next = p1 
                p1 = p1.next
            else:
                p.next = p2 
                p2 = p2.next
            p = p.next
        
        while p1 != None:
            p.next = p1
            p1 = p1.next 
            p = p.next 
        
        while p2 != None:
            p.next = p2 
            p2 = p2.next 
            p = p.next
        
        return newHead.next