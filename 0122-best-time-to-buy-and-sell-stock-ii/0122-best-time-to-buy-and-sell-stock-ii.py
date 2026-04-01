class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n =  len(prices)
        @cache
        def dp(buy,i):
            if i == n: 
                return 0
            
            if buy:
                return max(dp(False,i+1)-prices[i],dp(buy,i+1))

            return max(dp(True,i+1)+prices[i],dp(buy,i+1))
        return dp(True,0)
        