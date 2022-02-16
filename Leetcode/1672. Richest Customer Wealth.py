class Solution:
    @staticmethod
    def totalBalance(x):
        sum_list = 0
        for i in x:
            sum_list += i
        return sum_list

    def maximumWealth(self, accounts):
        res = []
        for i in accounts:
            res.append(self.totalBalance(i))
        res.sort()
        return res[-1]


s = Solution()
print(s.maximumWealth([[1, 2, 3], [3, 2, 1]]))
