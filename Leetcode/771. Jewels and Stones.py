class Solution:
    def numJewelsInStones(self, jewels, stones):
        res = 0
        for i in jewels:
            res += stones.count(i)
        return res


s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))