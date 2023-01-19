# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        isvisited = set()
        current = head
        while current:
            if current in isvisited:
                return True
            else:
                isvisited.add(current)
            current = current.next
        return False
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False