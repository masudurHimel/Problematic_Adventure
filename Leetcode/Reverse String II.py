class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        len_str = len(s)
        res = ""
        k = min(k,len_str)
        flag = False
        for i in enumerate(s):
            if i[0]% (2*k) == 0:
                _ = s[i[0]:i[0]+k]
                res = res + _[::-1]
            elif i[0]%k == 0:
                res = res + s[i[0]:i[0]+k]
        return res