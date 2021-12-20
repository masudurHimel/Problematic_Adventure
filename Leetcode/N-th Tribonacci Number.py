class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return min(n, 1)
        res = [0, 1, 1]
        for i in range(3, n + 1):
            res.append(res[i - 1] + res[i - 2] + res[i - 3])
        return res[-1]


x = Solution()
print(x.tribonacci(30))