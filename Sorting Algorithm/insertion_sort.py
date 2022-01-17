# Time Complexity : O(n^2)
# Space Complexity : O(n)
# Algorithmic Paradigm: Incremental Approach
# Sorting In Place: Yes
# Stable: Yes
# developed by John Mauchly(American physicist) in 1946


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print([i for i in arr])
