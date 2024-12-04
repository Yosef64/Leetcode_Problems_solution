class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        countZero , n = 0 , len(arr)
        for ele in arr:
            if ele == 0:countZero+=1
        
        tempArr = [0]*(n+countZero)
        f,s = 0, 0
        while f < n:
            tempArr[s] = arr[f]
            if arr[f] == 0:
                s += 1
            s += 1
            f += 1
        for ind in range(n):
            arr[ind] = tempArr[ind]
            

        