from functools import lru_cache


@lru_cache()
def tri(n: int) -> int:
    if n <= 1:
        return n
    if n == 2:
        return 1
    return tri(n - 1) + tri(n - 2) + tri(n - 3)


class Solution:
    def tribonacci(self, n: int) -> int:
        return tri(n)


x = Solution()
print(x.tribonacci(30))
