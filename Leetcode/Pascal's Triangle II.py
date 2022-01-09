class Solution:
    def getRow(self, rowIndex):
        rowIndex = rowIndex + 1
        res = [[1]]
        for i in range(1, rowIndex):
            list1 = res[i - 1] + [0]
            list2 = [0] + res[i - 1]
            _ = [a + b for a, b in zip(list1, list2)]
            res += [_]
        return res[-1]


s = Solution()
print(s.getRow(3))
