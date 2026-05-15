class Solution:
    def findMin(self, arr):

        s, e = 0, len(arr) - 1

        while s < e:

            mid = s + (e - s) // 2

            # Minimum is in right half
            if arr[mid] > arr[e]:
                s = mid + 1

            # Minimum is in left half including mid
            else:
                e = mid

        return arr[s]