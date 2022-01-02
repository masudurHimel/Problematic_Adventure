class Solution(object):
    def countBits(self, num):
        res = [0]
        while len(res) <= num:
            _ = [i+1 for i in res]
            res += _
        return res[:num+1]


s = Solution()
print(s.countBits(25))