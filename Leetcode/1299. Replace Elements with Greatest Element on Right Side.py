class Solution:
    def replaceElements(self, arr):
        while True:
            temp = arr[0]
            for i in enumerate(arr[1:]):
                ind = i[0] + 1
                if ind <= len(arr) or (arr[ind-1] == -1 and arr[ind+1] == -1):
                    continue
                if temp < i[1]:
                    arr[ind-1] = i[1]
                    arr[ind] = -1
                temp = i[1]

        return arr
s = Solution()
print(s.replaceElements([17, 18, 5, 4, 6, 1]))
