class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        _ = nums.count(0)
        for i in range(_):
            nums.remove(0)
            nums.append(0)