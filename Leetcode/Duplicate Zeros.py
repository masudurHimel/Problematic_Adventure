class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        flag = 0
        len_arr = len(arr)
        for i in range(len_arr):
            if flag == 1:
                flag = 0
                continue
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                flag = 1

        arr[:] = arr[:len_arr]