class Solution:
    def rob(self, nums):
        res = [0] * len(nums)
        res[0], res[1] = nums[0], nums[1]

        for i in enumerate(nums[2:]):
            max_val = 0
            for j in nums[:2 + i[0] - 1]:
                if j >= max_val:
                    max_val = j
            res[2 + i[0]] = max_val + i[1]
        return res


s = Solution()
x = [2, 7, 9, 3, 1]
print(s.rob(x))
