class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (high + 1)  # DP table to store the number of good strings ending at each length
        dp[0] = 1  # Base case: one way to have a string of length 0 (the empty string)

        for length in range(1, high + 1):
            # Add contributions from previous states
            if length >= zero:
                dp[length] += dp[length - zero]
            if length >= one:
                dp[length] += dp[length - one]
            dp[length] %= MOD

        # Sum up the results for lengths in the range [low, high]
        result = sum(dp[length] for length in range(low, high + 1)) % MOD
        return result
