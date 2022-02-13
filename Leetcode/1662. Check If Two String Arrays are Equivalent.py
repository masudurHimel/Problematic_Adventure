class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        res, res2 = '', ''
        for i in word1:
            res += i
        for i in word2:
            res2 += i
        return res == res2


s = Solution()
print(s.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]))
