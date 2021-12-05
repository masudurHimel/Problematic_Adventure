import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_ln = len(s1)
        s2_ln = len(s2)
        s1 = collections.Counter(s1)
        for i in range(s2_ln):
            _ = collections.Counter(s2[i:i+s1_ln])
            if _&s1==s1:
                return True
        return False