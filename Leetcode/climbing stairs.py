class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0,1,2]
        if n <= 2:
            return res[n]
        for i in range(3,n+1):
            res.append(res[i-1] + res[i-2])
        return res[-1]
s = Solution()
print(s.climbStairs(5))