# Definition for a binary tree node.
import math
from collections import Counter, deque
from copy import deepcopy


class Solution:
    def maxSubArray(self, nums):
        # combined = [nums[-1]] * len(nums)
        greedy = [nums[-1]] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            # combined[i] = combined[i+1]+nums[i]
            greedy[i] = max(nums[i], greedy[i+1]+nums[i])

        return max(greedy)


s = Solution()
x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(x))
