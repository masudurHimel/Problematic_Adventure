class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        res = nums1 + nums2
        res = sorted(res)
        print(res)
        if len(res) % 2 == 0:
            return (res[len(res) // 2] + res[len(res) // 2 - 1]) / 2
        else:
            return res[len(res) // 2]


s = Solution()
x, y = [1, 3], [2]
print(s.findMedianSortedArrays(x, y))
