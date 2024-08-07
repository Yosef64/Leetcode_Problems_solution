class Solution:
    def rob(self, nums: List[int]) -> int:
        ls = [0] * len(nums)
        if len(nums) <= 2:
            return max(nums)
            
        ls[0],ls[1],ls[2] = nums[0],nums[1],nums[0]+nums[2]
        ind = 0
        for i in range(3,len(nums)):
            ls[i]=max(nums[i]+ls[ind],nums[i]+ls[ind+1])
            ind += 1
       
        return max(ls[-1],ls[-2])