class Solution:
    def maxArea(self, height) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0

        while start <= end:
            if height[start] <= height[end]:
                _ = (end - start) * height[start]
                start += 1
            else:
                _ = (end - start) * height[end]
                end -= 1

            if _ > max_area:
                max_area = _
        return max_area


s = Solution()
print(s.maxArea([1, 1]))
