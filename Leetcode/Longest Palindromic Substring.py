class Solution:
    def longestPalindrome(self, s: str):
        res = None
        max_len = 0
        for i in enumerate(s):
            for j in range(len(s[:i[0] + 1])):
                if s[j] == s[i[0]]:
                    _ = self.isPalindrome(s[j:i[0] + 1], len(s[j:i[0]+1]))
                else:
                    _ = False
                if _ and _ > max_len:
                    max_len = _
                    res = s[j:i[0] + 1]
                    break
        return res

    def isPalindrome(self, s, len_s):
        if len_s%2 != 0:
            _ = s[len_s//2 + 1:]
        else:
            _ = s[len_s//2:]
        if s[:len_s // 2] == _[::-1]:
            return len_s
        else:
            return False



sa = Solution()
print(sa.longestPalindrome("aacabdkacaa"))
