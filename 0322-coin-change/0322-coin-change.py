class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(cur):
            if cur == 0 or cur < 0:
                return 0 if cur == 0 else float("inf")
            Min = float("inf")
            for coin in coins:
                Min = min(Min,1+dp(cur-coin))
            return Min
        res = dp(amount)
        return res if res != float("inf") else -1


        
        