class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for row in range(n):
            dp[row][row] = True
            for col in range(row-1,-1,-1):
                if s[row] == s[col]:
                    dp[row][col] = True if dp[row-1][col+1] or row-1==col else False
        @cache
        def df(cur):
            if cur == n:
                return 0
            ans = n - cur
            for ind in range(cur,n):
                if dp[ind][cur]:
                    ans = min(ans,df(ind+1)+1)
            return ans
        return df(0) - 1


        