class Solution:
    def convert(self, s, numRows):
        if numRows <= 1:
            return s
        res = [''] * numRows
        i = 0
        flag = 'pos'
        for j in s:
            res[i] += j

            if i >= numRows - 1:
                flag = 'neg'
            elif i <= 0:
                flag = 'pos'

            i = i + 1 if flag == 'pos' else i - 1

        return ''.join(res[:])


s = Solution()
print(s.convert(s="ABCDEFGH", numRows=3))
