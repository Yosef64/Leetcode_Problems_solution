class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        if arr[0] != 1:arr[0] = 1
        for ind in range(1,len(arr)):
            if arr[ind] > arr[ind-1]:
                arr[ind] = arr[ind-1]+1
        return arr[-1]

        