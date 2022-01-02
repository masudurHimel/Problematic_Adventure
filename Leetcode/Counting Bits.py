class Solution:
    def countBits(self, n):
        res = []
        for i in range(n+1):
            _ = bin(i)[2:]
            res.append(_.count('1'))
        return res


s = Solution()
print(s.countBits(5))