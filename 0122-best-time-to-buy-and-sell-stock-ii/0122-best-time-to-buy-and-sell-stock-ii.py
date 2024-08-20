class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(ind,buy):
            if ind == len(prices):
                return 0
            
            if buy:
                return max(dp(ind+1,False) - prices[ind],dp(ind+1,True))
            
            return max(prices[ind]+dp(ind+1,True),dp(ind+1,False))
        return dp(0,True)