# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        
        for i in range(0, n):
            if fast.next is None:
                return head.next
            fast = fast.next
        
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        if slow.next is not None:
            slow.next = slow.next.next
        
        return head