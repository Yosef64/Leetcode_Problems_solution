class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dp(buy,ind,count):
            if ind == len(prices) or count > k:
                return 0
            profit = 0
            if buy:
                profit = max(dp(False,ind+1,count) - prices[ind],dp(True,ind+1,count))
            else:
                profit = max(dp(True,ind+1,count+1)+prices[ind],dp(False,ind+1,count))
            return profit
        return dp(True,0,1)