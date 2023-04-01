from bisect import bisect_left, bisect_right
from collections import Counter
from math import *
import math
from collections import defaultdict, deque
from sortedcontainers import SortedList, SortedSet, SortedDict


from sortedcontainers import SortedList

from collections import defaultdict


class Solution:
    def maxSatisfaction(self, sa):
        sa = sorted(sa)
        n = len(sa)

        lastSum = 0
        curSum = 0
        i = n - 1
        while i >= 0 and sa[i] > 0:
            curSum += sa[i]
            lastSum += curSum
            i -= 1
        if i == -1 or lastSum == 0:
            return lastSum

        best = lastSum

        while i >= 0:
            curSum += sa[i]
            lastSum += curSum
            best = max(best, lastSum)
            i -= 1
        return best


s = Solution()
x = [-1, -8, 0, 5, -9]

print(s.maxSatisfaction(x))
