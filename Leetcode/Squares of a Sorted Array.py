class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        x = [i**2 for i in nums]
        x = sorted(x)
        return x