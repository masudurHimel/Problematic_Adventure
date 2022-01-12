class Solution:
    def rob(self, nums):
        if len(nums) <= 1:
            return nums[0]
        res = [0] * len(nums)
        visited = [0] * len(nums)
        res[0], res[1] = nums[0], nums[1]

        for i in enumerate(nums[2:]):
            max_val = 0
            if i[0] + 3 == len(nums):
                for j in enumerate(res[1:2 + i[0] - 1]):
                    if j[1] >= max_val and visited[j[0] + 1] == 0:
                        max_val = j[1]
            else:
                for j in enumerate(res[:2 + i[0] - 1]):
                    if j[1] >= max_val:
                        if j[0] == 0 or visited[j[0]] == 1:
                            visited[i[0] + 2] = 1
                        else:
                            visited[i[0] + 2] = 0
                        max_val = j[1]

            res[2 + i[0]] = max_val + i[1]
        return max(res)


s = Solution()
x = [1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3]
print(s.rob(x))
