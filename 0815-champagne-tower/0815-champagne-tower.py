class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0 for _ in range(query_row+1)]
        dp[0] = poured
        for ind in range(1,query_row+1):
            for i in range(ind,-1,-1):
                dp[i] = max((dp[i]-1)/2,0)
                if i != 0:
                    dp[i] += max((dp[i-1]-1)/2,0)
        return dp[query_glass] if dp[query_glass] <= 1 else 1.0
        