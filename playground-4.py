from bisect import bisect_left, bisect_right
from collections import Counter
from math import *
import math
from collections import defaultdict, deque
from sortedcontainers import SortedList, SortedSet, SortedDict


from sortedcontainers import SortedList

from collections import defaultdict


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_collection = defaultdict(list)
        odd_collection = defaultdict(list)

        s1 = list(s1)
        s2 = list(s2)

        for i in range(len(s1)):
            if i % 2 == 0:
                even_collection[s1[i]].append(i)
            else:
                odd_collection[s1[i]].append(i)

        # print(even_collection, odd_collection)

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                target = s2[i]
                if i % 2 == 0:
                    if even_collection.get(target):
                        temp = even_collection[target].pop(0)
                        s1[i], s1[temp] = s1[temp], s1[i]
                    else:
                        return False
                else:
                    if odd_collection.get(target):
                        temp = odd_collection[target].pop(0)
                        s1[i], s1[temp] = s1[temp], s1[i]
                    else:
                        return False

        # if s1[-2:] == s2[-2:]:
        #     return True
        return True


s = Solution()
x = "ublnlasppynwgx"
y = "ganplbuylnswpx"

print(s.checkStrings(x,y))
