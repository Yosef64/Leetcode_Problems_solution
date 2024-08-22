class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        dp = [[0 for _ in range(ind)] for ind in range(1,len(t)+2)]
        for ind in range(len(t)-1,-1,-1):
            for i in range(ind+1):
                # print(t[ind][i])
                dp[ind][i] = min(dp[ind+1][i],dp[ind+1][i+1]) + t[ind][i]
            
        return dp[0][0]