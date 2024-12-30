class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        for ind in range(high,-1,-1):
            if ind + one <= high:
                dp[ind] += dp[ind + one]
            if ind + zero <= high:
                dp[ind] += dp[ind + zero]
           
            dp[ind] += int(low <= ind <= high)
        return (dp[0]) % ( 10**9 + 7)