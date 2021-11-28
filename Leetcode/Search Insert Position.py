class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            l = 0
            r = len(nums) - 1
            p = (l + r) // 2

            if target > nums[-1]:
                return len(nums)
            if target < nums[0]:
                return 0

            while l < r:
                if l == p or r == p:
                    break
                if target < nums[p]:
                    r = p
                    p = (l + r) // 2
                else:
                    l = p
                    p = (l + r) // 2

            return l + 1
