class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof , min_stock = 0, prices[0]

        for i in range(1,len(prices)):
            max_prof = max(max_prof,prices[i]-min_stock)
            min_stock = min(min_stock,prices[i])
        return max_prof
        