class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        for num in range(1,amount+1):
            for coin in coins:
                if num - coin >= 0:
                    
                    dp[num] = min(dp[num], 1 + dp[num-coin])
                
                  
        
        return dp[-1] if dp[-1] != amount + 1 else -1
                    
        
        