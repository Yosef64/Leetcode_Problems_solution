class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for col in range(len(s)):
            dp[col][col] = True
            for row in range(col):
                if s[row] == s[col] and (col-row <= 2 or dp[row+1][col-1]):
                    dp[row][col] = True
                    ans += 1
        return ans