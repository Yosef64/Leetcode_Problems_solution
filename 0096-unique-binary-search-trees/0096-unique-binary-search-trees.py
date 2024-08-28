class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for num in range(2,n+1):
            dp[num] = dp[num-1]
            for i in range(1,num):
                Max = max(dp[num-i]*dp[i-1],max(dp[num-i],dp[i-1]))
                # print((num,i),Max)
                dp[num] += Max
            # print(num,dp[num])
        return dp[n]


        