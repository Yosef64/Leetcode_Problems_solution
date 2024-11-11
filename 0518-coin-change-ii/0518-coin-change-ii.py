class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(ind,amt):
            if ind == len(coins) or amt <= 0:
                return int(amt == 0)
            
            return dp(ind,amt-coins[ind])+dp(ind+1,amt)
        return dp(0,amount)
            