class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def isValid(arr):
            first , second = arr[:len(arr)//2] , arr[len(arr)//2:]
            for ind in range(1,len(first)):
                if first[ind] <= first[ind-1]:return False
            for ind in range(1,len(second)):
                if second[ind] <= second[ind-1]:return False
            return True
            
        for ind in range(len(nums)-k*2+1):
            # print(ind,ind+k*2)
            if isValid(nums[ind:ind+k*2]):return True
        return False
            