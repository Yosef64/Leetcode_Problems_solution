class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for num in range(2,n+1):
            dp[num] = dp[num-1]*2
            for i in range(2,num):
                dp[num] += dp[num-i]*dp[i-1]
        return dp[n]


        