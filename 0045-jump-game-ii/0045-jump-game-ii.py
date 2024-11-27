class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def dp(ind):
            if ind >= len(nums)-1:
                return 0
            res = float("inf")
            for jump in range(1,nums[ind]+1):
                res = min(res,1+dp(ind+jump))
            return res
        return dp(0)
