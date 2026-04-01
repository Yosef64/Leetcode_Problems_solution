class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dp(ind):
            if ind >= len(nums) - 1:
                return 0

            if ind in memo:
                return memo[ind]
            cur_min = float("inf")
            for i in range(1,nums[ind]+1):
                cur_min = min(cur_min,1+dp(ind+i))
            
            memo[ind] = cur_min
            return cur_min
        return dp(0)
