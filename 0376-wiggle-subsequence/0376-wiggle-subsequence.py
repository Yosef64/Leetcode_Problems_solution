class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [[1,1] for _ in range(len(nums))]
        ans = 0
        for ind in range(len(nums)):
            for dpI in range(ind):
                if nums[ind] > nums[dpI]:
                    dp[ind][0] = max(dp[ind][0],1+dp[dpI][1])
                elif nums[ind] < nums[dpI]:
                    dp[ind][1] = max(dp[ind][1],1+dp[dpI][0])
            ans = max(ans,max(dp[ind]))
        return ans