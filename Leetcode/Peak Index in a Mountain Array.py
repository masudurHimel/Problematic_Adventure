class Solution:
    def peakIndexInMountainArray(self, arr):
        l, m, h = 0, len(arr) // 2, len(arr) - 1
        while l < m:
            if arr[m] >= arr[m - 1]:
                l = m
                m = (m + h) // 2
            else:
                h = m
                m = (l + m) // 2
        return m


s = Solution()
print(s.peakIndexInMountainArray([18, 29, 38, 59, 98, 100, 99, 98, 90]))
