class Solution:
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            list1 = res[i-1] + [0]
            list2 = [0] + res[i-1]
            _ = [a + b for a, b in zip(list1, list2)]
            res += [_]
        return res



s = Solution()
print(s.generate(30))
