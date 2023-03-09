# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        new_head = ListNode()
        p = new_head
        while head1 and head2:
            if head1.val < head2.val:
                p.next = head1
                head1 = head1.next
            else:
                p.next = head2
                head2 = head2.next
            p = p.next
        
        if head1:
            p.next = head1
        if head2:
            p.next = head2
        return new_head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            results = []
            for i in range(0, len(lists), 2):
                temp1 = lists[i]
                temp2 = lists[i+1] if (i+1) < len(lists) else None
                merged = self.merge(temp1, temp2)
                results.append(merged)
            lists = results
        
        return lists[0]
        