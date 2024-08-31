class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n for _ in range(n+1)]
        dp[0] = 0
        for num in range(1,n+1):
            for sq in range(int(sqrt(num))+1):
                dp[num] = min(dp[num],1+dp[num-sq**2])
        return dp[-1]
        