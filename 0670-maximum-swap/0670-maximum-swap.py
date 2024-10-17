class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = list(str(num))
        for ind in range(len(arr)):
            maxInd = ind
            for ind1 in range(ind+1,len(arr)):
                if arr[maxInd] < arr[ind1] or (arr[maxInd] == arr[ind1] and maxInd!=ind):
                    maxInd = ind1  
            if maxInd > ind:
                print(arr[maxInd],arr[ind])
                arr[maxInd] , arr[ind] = arr[ind] , arr[maxInd]
                break
        return int("".join(arr))