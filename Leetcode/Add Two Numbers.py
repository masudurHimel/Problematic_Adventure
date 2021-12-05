# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res1 = ''
        res2 = ''
        head1 = l1
        head2 = l2
        while l1:
            res1 = str(l1.val) + res1
            l1 = l1.next

        while l2:
            res2 = str(l2.val) + res2
            l2 = l2.next

        res1, res2 = int(res1), int(res2)
        res = res1 + res2
        target = head1 if res1 >= res2 else head2
        temp_head = head1
        while res != 0:
            temp_head.val = res % 10
            res = res // 10
            if temp_head.next == None and res != 0:
                temp_head.next = ListNode()
            temp_head = temp_head.next
        return head1