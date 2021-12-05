# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = head
        h = head
        for i in range(n):
            h = h.next
        if not h:
            return head.next
        while h.next:
            h = h.next
            l = l.next
        l.next = l.next.next
        return head