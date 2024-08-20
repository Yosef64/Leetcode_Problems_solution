class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 1:
            return nums[0]
        if L == 2 or L == 3:
            return  max(nums)           
        first = [0,nums[1]]
        second = [nums[0],0]
        for i in range(2,L-1):
            first = [max(first),first[0]+nums[i]]
            second = [max(second),second[0]+nums[i]]
        first = max([max(first),first[0]+nums[L-1]]) 
        second = max(second)
        return max(first,second)
        