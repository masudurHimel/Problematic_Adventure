class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        res = [0,1]
        for i in range(2, n + 1):
            res.append(res[i - 1] + res[i - 2])
        return res[-1]


x = Solution()
print(x.fib(3))
