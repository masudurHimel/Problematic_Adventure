class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        his = []
        max_i = 0
        for i in s:
            if i in his:
                his = his[his.index(i) + 1:]
            his.append(i)
            max_i = max(len(his), max_i)
        return max_i

