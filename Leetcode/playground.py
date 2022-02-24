class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None
        res = [head.val]
        head = head.next
        while head:
            if res[-1] != head.val:
                res.append(head.val)
            head = head.next

        flag = 0
        for i in res:
            if flag == 0:
                res_head = ListNode(val=i)
                tmp_head = res_head
                flag = 1
            else:
                _ = ListNode(val=i)
                tmp_head.next = _
                tmp_head = _
        return res_head


s = Solution()
head = ListNode(val=1, next=ListNode(val=1, next=(ListNode(val=2))))
print(s.deleteDuplicates(head))
