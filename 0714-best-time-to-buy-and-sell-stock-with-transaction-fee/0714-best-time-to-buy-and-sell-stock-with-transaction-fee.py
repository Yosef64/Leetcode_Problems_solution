class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def dp(ind,buy):
            if ind == len(prices):
                return 0
            if (ind,buy) in memo:return memo[(ind,buy)]

            if buy:
                profit = max(dp(ind+1,0) - prices[ind]-fee,dp(ind+1,1))
            else:
                profit = max(dp(ind+1,1)+prices[ind],dp(ind+1,0))
            
            memo[(ind,buy)] = profit
            return memo[(ind,buy)]
        return dp(0,1)
