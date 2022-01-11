class Solution:
    def reverse(self, x):
        if x < 0:
            x = int('-' + str(abs(x))[::-1])
        else:
            x = int(str(x)[::-1])
        if x > pow(2, 31):
            return 0
        return x


s = Solution()
print(s.reverse(-1563847412))
