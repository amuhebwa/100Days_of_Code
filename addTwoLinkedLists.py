# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        newHead = ListNode(0)
        p = newHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 
            total = carry + val1 + val2
            carry = total//10
            _new = ListNode(total%10)
            p.next = _new
            p = _new
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return newHead.next





