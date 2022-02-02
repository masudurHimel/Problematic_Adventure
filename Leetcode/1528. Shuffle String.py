class Solution:
    def restoreString(self, s, indices):
        res = {}
        for i, x in enumerate(s):
            res[indices[i]] = x

        res_str = ""
        for i in range(len(s)):
            res_str += res[i]

        return res_str


s = Solution()
print(s.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
