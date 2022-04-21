# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def traverseList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        x = sorted(nums.copy(), reverse=True)
        for i in enumerate(nums):
            _ = x.count(i[0])
            nums[i[0]] = len(nums) - x.index(i[1]) -1
            if _ > 1:
                nums[i[0]] -= _ -1
        return nums



s = Solution()
list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4)))
list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))
print(s.smallerNumbersThanCurrent([8,1,2,2,3]))
