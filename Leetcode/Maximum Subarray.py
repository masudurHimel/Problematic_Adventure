class Solution:
    def maxSubArray(self, nums):
        max_res = nums[0]
        res = [0] * len(nums)
        res[0] = nums[0]
        for i in enumerate(nums[1:]):
            _ = i[1] + res[i[0]]
            if _ > i[1]:
                res[i[0]+1] = _
            else:
                res[i[0]+1] = i[1]
            if max_res < res[i[0]+1]:
                max_res = res[i[0]+1]
        return max_res


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
