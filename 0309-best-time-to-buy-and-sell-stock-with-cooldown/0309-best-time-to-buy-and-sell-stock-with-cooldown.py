class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(ind,buy):
            if ind >= len(prices):
                return 0
            
            if buy:
                return max(dp(ind+1,False)-prices[ind],dp(ind+1,buy))
            
            return max(dp(ind+2,True)+prices[ind],dp(ind+1,buy))
        return dp(0,True)
        
