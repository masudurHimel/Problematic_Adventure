# Time Complexity : T(n) = 2T(n/2) + θ(n) => O(nlogn)
# Space Complexity : O(n)
# Algorithmic Paradigm: Divide and Conquer
# Sorting In Place: No
# Stable: Yes
# Invented by John von Neumann in 1945

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    mergeSort(arr)
    print([i for i in arr])
