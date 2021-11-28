class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        flag = 0
        for x in nums:
            if x == 1:
                flag = flag +1
            else:
                flag = 0
            res = max(res, flag)

        return res