class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        max_sum = 0
        while k!=0:
            while k!=0 and numOnes!=0:
                max_sum+=1
                numOnes-=1
                k-=1
            if k==0:
                return max_sum
            while k!=0 and numZeros!=0:
                numZeros-=1
                k-=1
            if k==0:
                return max_sum
            while k!=0 and numNegOnes!=0:
                max_sum-=1
                numNegOnes-=1
                k-=1
        return max_sum
            
        