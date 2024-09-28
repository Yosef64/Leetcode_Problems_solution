class Solution:
    def maximumTotalSum(self, maxH: List[int]) -> int:
        maxH.sort()
        res = maxH[-1]
        for ind in range(len(maxH)-2,-1,-1):
            if maxH[ind] >= maxH[ind+1]:
                maxH[ind] = maxH[ind+1] - 1
            if maxH[ind] <= 0:
                return -1
            res += maxH[ind]
        
        return res

        