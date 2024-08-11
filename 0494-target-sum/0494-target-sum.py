class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(ind,cur):
            if ind == len(nums):
                return cur == target
            
            if (ind,cur) in memo:return memo[(ind,cur)]

            memo[(ind,cur)] = dp(ind+1,cur+nums[ind]) + dp(ind+1,cur-nums[ind])
            return memo[(ind,cur)]
        return dp(0,0)