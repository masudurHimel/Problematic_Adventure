class Solution:
    def maxProfit(self, prices):
        min_v = 999999999999
        max_v = 0
        for i in prices:
            if i < min_v:
                min_v = i
            if (i - min_v) > max_v:
                max_v = i - min_v
        return max_v


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
