# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        p = (l + r) // 2

        while l <= r:
            if isBadVersion(p) == False:
                l = p + 1
                p = (l + r) // 2
            else:
                flag = p
                r = p - 1
                p = (l + r) // 2
        return flag