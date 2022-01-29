class Solution:
    def mostWordsFound(self, sentences):
        max_len = 0
        for i in sentences:
            _ = i.count(' ')
            if max_len < _:
                max_len = _
        return max_len + 1


s = Solution()
print(s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
