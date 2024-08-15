class Solution(object):
    def countVowelStrings(self, n):
        dp = [[0] * 5 for _ in range(n + 1)]

        for j in range(5):
            dp[1][j] = 1

        for i in range(2, n + 1):
            for j in range(5):
                for k in range(j, 5):
                    dp[i][j] += dp[i - 1][k]

        result = sum(dp[n])
        return result