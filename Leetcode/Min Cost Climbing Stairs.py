class Solution:
    def minCostClimbingStairs(self, cost):
        res = [0] * len(cost)
        for i in range(2, len(cost)):
            a, b = res[i - 1] + cost[i - 1], res[i - 2] + cost[i - 2]
            res[i] = min(a, b)
        return min((res[-1] + cost[-1]), res[-2] + cost[-2])


s = Solution()
print(s.minCostClimbingStairs([10, 15, 20]))
