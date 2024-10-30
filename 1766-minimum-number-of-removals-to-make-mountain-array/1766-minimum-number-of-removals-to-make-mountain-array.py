class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1,1] for _ in range(n)]

        for ind in range(n-2,-1,-1):
            for i in range(ind+1,n):
                if nums[ind] > nums[i]:
                    dp[ind][0] = max(dp[ind][0],1+dp[i][0])
        
        total , maxS = 0 , [1,0]
        for ind in range(1,n-1):
            for i in range(ind):
                if nums[ind] > nums[i]:
                    dp[ind][1] = max(dp[ind][1],1+dp[i][1])
            maxS = max(maxS,[dp[ind][1],ind])
            if nums[ind] != nums[ind+1] and maxS[0] > 1 and (dp[ind+1][0]!= 1 or (dp[ind+1][0]==1 and nums[ind+1] < nums[ind])):
                
                total = max(total,maxS[0]+dp[ind+1][0] if nums[maxS[1]] != nums[ind+1] else dp[ind][1] + dp[ind+1][0]) 
        return n - total