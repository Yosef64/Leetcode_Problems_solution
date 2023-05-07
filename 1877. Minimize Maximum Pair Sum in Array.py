class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        max=nums[i]+nums[j]
        while i<j:
            if max<nums[i]+nums[j]:
                max=nums[i]+nums[j]
            i+=1
            j-=1
        return max
            
        
        