class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums) - 1
        Min , ans = nums[-1] , 0
        for ind in range(n - 1,-1,-1):
            if nums[ind] <= Min:
                Min = nums[ind]
            else:
                ways = math.ceil(nums[ind] / Min) 

                ans += ways - 1
                
                Min = nums[ind] // ways

        return ans